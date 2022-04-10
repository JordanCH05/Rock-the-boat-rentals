from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Boat


def all_products(request):
    """ A view to show all boats """

    boat_list = Boat.objects.all()
    paginator = Paginator(boat_list, 40)

    page = request.GET.get('page')

    try:
        boats = paginator.get_page(page)
    except PageNotAnInteger:
        boats = paginator.get_page(1)
    except EmptyPage:
        boats = paginator.get_page(paginator.num_pages)

    nums = "a" * boats.paginator.num_pages
    page_min = boats.number - 5
    page_max = boats.number + 5
    page_range = range(page_min, page_max)
    context = {
        'boats': boats,
        'nums': nums,
        'page_range': page_range,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, boat_id):
    """ A view to show individual boat details """

    boat = get_object_or_404(Boat, pk=boat_id)

    context = {
        'boat': boat
    }

    return render(request, 'products/product_detail.html', context)
