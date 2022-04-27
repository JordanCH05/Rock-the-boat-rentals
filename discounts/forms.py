from django import forms

from .models import Coupon


class CouponForm(forms.ModelForm):
    code = forms.CharField()

    class Meta:
        model = Coupon
        fields = ('code',)
