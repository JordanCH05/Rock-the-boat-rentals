import stripe
import json
from decimal import Decimal

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from currencies.models import Currency
from products.models import Boat
from discounts.models import Coupon
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import fleet_contents
from currency.contexts import currencies


@require_POST
def cache_checkout_data(request):
    """ Cache Checkout Data """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.modify(pid, metadata={
            'fleet': json.dumps(request.session.get('fleet', [])),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as ex:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=ex, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    total = fleet_contents(request)['grand_total']
    stripe_total = round(total * 100)

    currency = request.session.get('currency', settings.DEFAULT_CURRENCY)
    if stripe_total > 99999999:
        if currency == 'GBP':
            messages.error(request, "The total price exceeded the €999,999.99 \
                payment limit, please try seperate payments")
            return redirect(reverse('view_bag'))
        else:
            messages.error(request, f"The total price exceeded the 999,999.99 \
                {currency} payment limit, so the currency has been changed \
                    back to the default: {settings.DEFAULT_CURRENCY}.")
            currency = settings.DEFAULT_CURRENCY
            request.session['currency'] = settings.DEFAULT_CURRENCY

    if request.method == 'POST':
        fleet = request.session.get('fleet', {})
        if not fleet:
            messages.error(request,
                           "There's nothing in your fleet at the moment")
            return redirect(reverse('products'))

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            factor = currencies(request)['factor']
            cur_currency = Currency.objects.get(code=currency)
            order.currency = cur_currency
            order.stripe_pid = pid
            order.original_bag = fleet
            delivery_threshold = settings.FREE_SHIPPING_THRESHOLD * factor
            order.delivery_threshold = delivery_threshold
            coupon_id = request.session.get('coupon_id', None)
            if coupon_id:
                coupon = Coupon.objects.get(id=coupon_id)
                order.coupon = coupon
                order.discount = fleet_contents(request)['discount']
            order.save()
            for sku, quantity in fleet.items():
                try:
                    boat = Boat.objects.get(sku=sku)
                    price = boat.price
                    divisor = Decimal(boat.currency.factor)
                    converter = factor/divisor
                    price = price * converter
                    lineitem_total = price * quantity
                    order_line_item = OrderLineItem(
                        order=order,
                        boat=boat,
                        quantity=quantity,
                        lineitem_total=lineitem_total,
                    )
                    order_line_item.save()

                except Boat.DoesNotExist:
                    messages.error(request, (
                        "One of the boats in your fleet wasn't found in our"
                        " database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]
                ))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=currency,
        )

        # Attempt to prefill the form with any info the user maintains in
        # their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'fleet' in request.session:
        del request.session['fleet']

    if 'coupon_id' in request.session:
        del request.session['coupon_id']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
