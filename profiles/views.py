from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm
from reviews.forms import ReviewForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed.'
                           ' Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    boat_list = []
    for order in orders:
        items = order.lineitems.all()
        for item in items:
            boat = item.boat
            if boat not in boat_list:
                boat_list.append(boat)

    review = ReviewForm()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'boat_list': boat_list,
        'review': review,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Order History """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a post confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
