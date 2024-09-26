from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django import forms
from .models import *


class Trade4meForm(forms.ModelForm):
    class Meta:
        model = Trade4me
        fields = ['full_name','email','login_ID','password']

        