from decimal import Decimal
from currencies.models import Currency
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE/100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


def currencies(request):

    suffix_cur = ['DKK', 'CHF']
    currency = settings.DEFAULT_CURRENCY

    if request.GET:
        if 'currency' in request.GET:
            currency = request.GET['currency']

    filt_cur = Currency.objects.filter(code=currency).values()[0]
    factor = filt_cur['factor']
    symbol = filt_cur['symbol']
    name = filt_cur['name']
    name = name.split(' ')[-1]
    fa_cur = name.lower()
    print(fa_cur)

    context = {
        'suffix_cur': suffix_cur,
        'fa_cur': fa_cur,
        'current_cur': currency,
        'factor': factor,
        'symbol': symbol,
    }

    return context
