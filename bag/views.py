from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, boat):
    """ Add a boat to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    fleet = request.session.get('fleet', [])

    if boat in fleet:
        print('Already in fleet')
    else:
        fleet.append(boat)

    request.session['fleet'] = fleet
    print(request.session['fleet'])

    return redirect(redirect_url)
