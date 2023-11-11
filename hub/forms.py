from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Ranges


class RangesForm(forms.ModelForm):
    class Meta:
        model = Ranges
        exclude = ["coin"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
