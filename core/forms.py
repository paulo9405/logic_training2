from django import forms
from .models import DoubleSave


class DoubleForm(forms.ModelForm):
    class Meta:
        model = DoubleSave
        fields = ['value', 'double_value']