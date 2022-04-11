import operator
from functools import reduce
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Boat, Category


def all_products(request):
    """ A view to show all boats """

    query = None
    category = None
    cur_category = None
    boat_list = Boat.objects.all()

    if request.GET:

        if 'category' in request.GET:
            category = request.GET['category']
            if category is not None:
                boat_list = boat_list.filter(category__name=category)
                cur_category = Category.objects.filter(name=category)
                print(cur_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if query is not None:
                if not query:
                    messages.error(
                        request, "You didn't enter any search criteria!"
                        )
                    return redirect(reverse('products'))

                query = query.split(' ')

                queries = []

                for term in query:

                    q = (Q(category__name__icontains=term) |
                         Q(manufacturer__icontains=term) |
                         Q(condition__icontains=term) |
                         Q(fuel__icontains=term) |
                         Q(year_built__icontains=term) |
                         Q(material__icontains=term) |
                         Q(location__icontains=term)
                         )

                    queries.append(q)

                queries = reduce(operator.and_, queries)

                boat_list = boat_list.filter(queries)

    paginator = Paginator(boat_list, 40)

    page = request.GET.get('page')

    try:
        boats = paginator.page(page)
    except PageNotAnInteger:
        print('NOT AN INTEGER')
        boats = paginator.get_page(1)

    except EmptyPage:
        print('empty')
        boats = paginator.get_page(paginator.num_pages)

    nums = "a" * boats.paginator.num_pages
    page_min = boats.number - 5
    page_max = boats.number + 5
    page_range = range(page_min, page_max)

    context = {
        'boats': boats,
        'nums': nums,
        'page_range': page_range,
        'search_term': query,
        'current_category': cur_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, boat_id):
    """ A view to show individual boat details """

    boat = get_object_or_404(Boat, pk=boat_id)

    context = {
        'boat': boat
    }

    return render(request, 'products/product_detail.html', context)
