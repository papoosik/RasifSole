from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['title', 'category', 'season', 'collaboration', 'brand', 'color', 'material', 'description', 'price', 'picture_side', 'picture_forward', 'picture_back', 'picture_sole']