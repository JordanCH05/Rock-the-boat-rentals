from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponForm


@require_POST
def apply_coupon(request):
    now = timezone.now()
    coupon_form = CouponForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True,
            )
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(request, "Coupon does not exist")

    return render(request, 'bag/bag.html', {'coupon_form': coupon_form})
