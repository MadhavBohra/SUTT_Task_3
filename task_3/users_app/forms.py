import email
from socket import fromshare
from tokenize import Name
from django import forms
# importing user models(tables if you want to go with that terminology)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']