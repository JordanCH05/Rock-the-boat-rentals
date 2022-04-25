import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from products.models import Boat
from profiles.models import UserProfile
from currency.contexts import currencies
from .models import Order, OrderLineItem


class StripeWHHandler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order, suffix_cur):
        """ Send the user a confirmation email """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'suffix_cur': suffix_cur
            })

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print('Unhandled')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('success')
        intent = event.data.object
        pid = intent.id
        fleet = intent.metadata.fleet
        save_info = intent.metadata.save_info
        suffix_cur = currencies(self.request)['suffix_cur']

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=json.loads(fleet),
                    stripe_pid=pid,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
                print(f'Attempt: {attempt - 1}')
        if order_exists:
            self._send_confirmation_email(order, suffix_cur)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | '
                'SUCCESS: Verified order already in database',
                status=200
                )
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=json.loads(fleet),
                        stripe_pid=pid,
                    )
                for sku in json.loads(fleet):
                    boat = Boat.objects.get(sku=sku)
                    order_line_item = OrderLineItem(
                        order=order,
                        boat=boat,
                        lineitem_total=boat.price,
                    )
                    order_line_item.save()
            except Exception as ex:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {ex}',
                    status=500
                )
        self._send_confirmation_email(order, suffix_cur)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | '
                    'SUCCESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """
        print('failed')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
