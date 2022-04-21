from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    fleet = request.session.get('fleet', [])
    if not fleet:
        messages.error(request, "There's nothing in your fleet at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KRDiPEs7dUZiWua0gDCmiq735AHBG23Cm9XxGPa1VU4yM5czJc1DdRLx1HJ2qoQusJRO5oGj41ULezFqxwuzRpT00OdiKN3Co',
        'client_secret': 'test',
    }

    return render(request, template, context)
