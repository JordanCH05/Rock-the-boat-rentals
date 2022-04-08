from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Boat


def all_products(request):
    """ A view to show all boats """

    boat_list = Boat.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(boat_list, 40)
    try:
        boats = paginator.page(page)
    except PageNotAnInteger:
        boats = paginator.page(1)
    except EmptyPage:
        boats = paginator.page(paginator.num_pages)

    context = {
        'boats': boats,
    }

    return render(request, 'products/products.html', context)
