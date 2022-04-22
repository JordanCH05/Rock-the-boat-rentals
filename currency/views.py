from django.shortcuts import redirect
from django.contrib import messages
from currencies.models import Currency


def change_currency(request, currency, redirect_url=''):

    # If boat in fleet then prevent currency change

    redirect_url = '/' + redirect_url
    currencies = []
    filt_cur = Currency.objects.values()
    for cur in filt_cur:
        currencies.append(cur['code'])
    if currency in currencies:
        request.session['currency'] = currency
        messages.success(request, f"Currency changed to {currency}")
        return redirect(redirect_url)
    else:
        messages.error(request, f"Sorry, we don't use this currency: {currency}")
        return redirect(redirect_url)
