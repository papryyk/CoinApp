from django import forms

from .models import Ranges


class RangesForm(forms.ModelForm):
    class Meta:
        model = Ranges
        fields = ["min_range", "max_range", "symbol"]
        widgets = {
            "symbol": forms.HiddenInput()
        }
