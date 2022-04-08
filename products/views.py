from django.shortcuts import render
from .models import Boat


def all_products(request):
    """ A view to show all boats """

    boats = Boat.objects.all()

    context = {
        'boats': boats,
    }

    return render(request, 'products/products.html', context)
