from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Subscribe_User(forms.ModelForm):
    class Meta:
        model = Notified_list
        fields = '__all__'