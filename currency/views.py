from django.shortcuts import redirect, reverse
from django.contrib import messages
from currencies.models import Currency
from bag.contexts import fleet_contents


def change_currency(request, currency, redirect_url=''):

    # If boat in fleet then prevent currency change
    fleet_items = fleet_contents(request)['fleet_items']
    redirect_url = '/' + redirect_url
    if fleet_items:
        messages.warning(
            request,
            "Please empty your empty your fleet before changing currencies")
        return redirect(reverse('products'))
    else:
        currencies = []
        filt_cur = Currency.objects.values()
        for cur in filt_cur:
            currencies.append(cur['code'])
        if currency in currencies:
            request.session['currency'] = currency
            messages.success(request, f"Currency changed to {currency}")
            return redirect(reverse('products'))
        else:
            messages.error(request,
                           f"Sorry, we don't use this currency: {currency}")
            return redirect(reverse('products'))
