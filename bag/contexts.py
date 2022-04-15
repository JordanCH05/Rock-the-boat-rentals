from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from currencies.models import Currency
from products.models import Boat


def bag_and_currencies(request):

    suffix_cur = ['DKK', 'CHF']
    currency = settings.DEFAULT_CURRENCY

    if request.GET:
        if 'currency' in request.GET:
            currency = request.GET['currency']

    filt_cur = Currency.objects.filter(code=currency).values()[0]
    factor = filt_cur['factor']
    factor = Decimal(factor)
    symbol = filt_cur['symbol']

    name = filt_cur['name']
    name = name.split(' ')[-1]
    fa_cur = name.lower()

    total = 0
    product_count = 0
    fleet = request.session.get('fleet', [])
    fleet_items = []

    for sku in fleet:
        boat = get_object_or_404(Boat, sku=sku)
        price = boat.price
        divisor = Decimal(boat.currency.factor)
        converter = factor/divisor
        price = price * converter
        total += price
        fleet_items.append(boat)

    shipping_threshold = settings.FREE_SHIPPING_THRESHOLD * factor

    if total < shipping_threshold:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE/100)
        free_shipping_delta = shipping_threshold - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': shipping_threshold,
        'grand_total': grand_total,
        'fleet_items': fleet_items,
        'suffix_cur': suffix_cur,
        'fa_cur': fa_cur,
        'current_cur': currency,
        'factor': factor,
        'symbol': symbol,
    }

    return context
