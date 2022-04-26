from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm


@login_required
def add_review(request):
    """ Add a boat review """

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save()
            messages.success(request, 'Successfully reviewed boat!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to review boat.'
                           ' Please ensure the form is valid')
    else:
        review_form = ReviewForm()

    return redirect(reverse('profile'))
