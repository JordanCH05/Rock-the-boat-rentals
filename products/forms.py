from django import forms

from .models import Boat, Category
from .widgets import CustomClearableFileInput


class BoatForm(forms.ModelForm):
    """ Boat Form """

    class Meta:
        model = Boat
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-100 border-dark rounded-0'
