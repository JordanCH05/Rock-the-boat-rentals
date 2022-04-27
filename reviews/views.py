from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Boat
from .forms import ReviewForm


@login_required
def add_review(request, boat_id):
    """ Add a boat review """

    boat = get_object_or_404(Boat, pk=boat_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.username = request.user
            review.boat = boat
            review.save()
            messages.success(request, 'Successfully reviewed boat!')
            return redirect(reverse('product_detail', args=[boat.id]))
        else:
            messages.error(request, 'Failed to review boat.'
                           ' Please ensure the form is valid')
    else:
        review_form = ReviewForm(instance=boat)

    template = 'reviews/add_review.html'
    context = {
        'review_form': review_form,
        'boat': boat,
    }

    return render(request, template, context)
