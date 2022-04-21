import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import fleet_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    fleet = request.session.get('fleet', [])
    if not fleet:
        messages.error(request, "There's nothing in your fleet at the moment")
        return redirect(reverse('products'))

    total = fleet_contents(request)['grand_total']
    stripe_total = round(total * 100)

    currency = request.session.get('currency', settings.DEFAULT_CURRENCY)
    if stripe_total > 99999999:
        if currency == 'EUR':
            messages.error(request, "The total price exceeded the €999,999.99 \
                payment limit, please try seperate payments")
            return redirect(reverse('view_bag'))
        else:
            messages.error(request, f"The total price exceeded the 999,999.99 \
                {currency} payment limit, so the currency has been changed \
                    back to the deafult: {settings.DEFAULT_CURRENCY}.")
            currency = settings.DEFAULT_CURRENCY
            request.session['currency'] = settings.DEFAULT_CURRENCY

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=request.session.get('currency', settings.DEFAULT_CURRENCY),
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
