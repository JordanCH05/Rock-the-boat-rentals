from django import forms
from crispy_forms.helper import FormHelper

from .models import Review


class ReviewForm(forms.ModelForm):
    """ Review Form """

    score = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ('score', 'body')

    def __init__(self, *args, **kwargs):

        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
