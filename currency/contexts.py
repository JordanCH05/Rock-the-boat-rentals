from decimal import Decimal
from django.conf import settings
from currencies.models import Currency


def currencies(request):

    suffix_cur = ['DKK', 'CHF']
    currency = request.session.get('currency', settings.DEFAULT_CURRENCY)

    currency_objs = Currency.objects.all()

    if not currency_objs:
        filt_cur = []
        factor = 1
        symbol = '£'
        fa_cur = 'sterling'
    else:
        filt_cur = Currency.objects.filter(code=currency).values()[0]
        factor = filt_cur['factor']
        factor = Decimal(factor)
        symbol = filt_cur['symbol']

        name = filt_cur['name']
        name = name.split(' ')[-1]
        fa_cur = name.lower()

    context = {
        'suffix_cur': suffix_cur,
        'fa_cur': fa_cur,
        'current_cur': currency,
        'factor': factor,
        'symbol': symbol,
    }

    return context
