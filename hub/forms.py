from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Ranges


class RangesForm(forms.ModelForm):
    class Meta:
        model = Ranges
        exclude = ["coin"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = [forms.TextInput(attrs={'class': 'register_input'})]


class signInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'user_pwd', 'placeholder': 'Username', 'id': 'user-input'}), label='')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'user_pwd', 'placeholder': 'Password', 'id': 'user-pwd'}), label='')
