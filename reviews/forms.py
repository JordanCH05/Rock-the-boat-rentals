from django import forms
from crispy_forms.helper import FormHelper

from .models import Review

SCORE_CHOICES = [
    (5, '5 / 5 - Amazing'),
    (4, '4 / 5 - Good'),
    (3, '3 / 5 - OK'),
    (2, '2 / 5 - Bad'),
    (1, '1 / 5 - Terrible'),
    (0, '0 / 5 - Worst Boat Ever'),
]


class ReviewForm(forms.ModelForm):
    """ Review Form """

    class Meta:
        model = Review
        fields = ('score', 'body')

    def __init__(self, *args, **kwargs):

        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['score'] = forms.ChoiceField(choices=SCORE_CHOICES)
