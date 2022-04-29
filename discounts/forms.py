from django import forms

from .models import Coupon


class CouponForm(forms.ModelForm):
    code = forms.CharField()

    class Meta:
        model = Coupon
        fields = ('code',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['class'] = 'mx-2'
        self.fields['code'].label = 'Discount Code'
