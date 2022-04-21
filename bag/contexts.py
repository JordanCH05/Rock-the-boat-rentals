from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Boat
from currency.contexts import currencies


def fleet_contents(request):

    total = 0
    product_count = 0
    fleet = request.session.get('fleet', [])
    fleet_items = []
    factor = currencies(request)['factor']

    for sku in fleet:
        boat = get_object_or_404(Boat, sku=sku)
        price = boat.price
        divisor = Decimal(boat.currency.factor)
        converter = factor/divisor
        price = price * converter
        total += price
        fleet_items.append(boat)
        product_count += 1

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
        'factor': factor,
    }

    return context
