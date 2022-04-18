from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, boat):
    """ Add a boat to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    fleet = request.session.get('fleet', [])

    if boat in fleet:
        messages.info(request, f'{boat} already in your fleet')
    else:
        fleet.append(boat)
        messages.success(request, f'Added {boat} to your fleet')

    request.session['fleet'] = fleet

    return redirect(redirect_url)


def remove_from_bag(request, boat):
    """ Remove a boat from the shopping bag """

    try:
        fleet = request.session.get('fleet', [])

        fleet.remove(boat)
        messages.success(request, f'Removed {boat} from your fleet')

        request.session['fleet'] = fleet
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing boat: {e}')
        return HttpResponse(status=500)
