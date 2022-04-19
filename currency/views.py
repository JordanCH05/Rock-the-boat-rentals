from django.shortcuts import HttpResponse, redirect
from currencies.models import Currency


def change_currency(request, currency, redirect_url=''):

    redirect_url = '/' + redirect_url
    currencies = []
    filt_cur = Currency.objects.values()
    for cur in filt_cur:
        currencies.append(cur['code'])
    if currency in currencies:
        request.session['currency'] = currency
        return redirect(redirect_url)
    else:
        return HttpResponse(status=500)
