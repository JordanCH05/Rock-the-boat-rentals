from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Boat
from discounts.forms import CouponForm


def view_bag(request):
    """ A view that renders the bag contents page """

    coupon_form = CouponForm()

    context = {
        'coupon_form': coupon_form,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, boat_id):
    """ Add a boat to the shopping bag """

    boat = get_object_or_404(Boat, pk=boat_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    fleet = request.session.get('fleet', {})

    if boat.sku in fleet:
        fleet[boat.sku] += quantity
        messages.info(request, f'Updated quantity of: {boat.name}')
    else:
        fleet[boat.sku] = quantity
        messages.success(request, f'Added to your fleet: {boat.name}')

    request.session['fleet'] = fleet

    return redirect(redirect_url)


def remove_from_bag(request, boat_id):
    """ Remove a boat from the shopping bag """

    boat = get_object_or_404(Boat, pk=boat_id)
    try:
        fleet = request.session.get('fleet', {})

        fleet.pop(boat.sku)
        messages.success(request, f'Removed {boat.sku} from your fleet')

        request.session['fleet'] = fleet
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing boat: {e}')
        return HttpResponse(status=500)
