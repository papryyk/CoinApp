from django import forms

from .models import Ranges


class RangesForm(forms.ModelForm):
    class Meta:
        model = Ranges
        exclude = ["coin"]
