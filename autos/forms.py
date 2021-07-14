from django import forms
from django.forms import ModelForm
from .models import *


class MakeForm(forms.ModelForm):
    class Meta:
        model = MakeCreate
        fields = "__all__"


class AutosForm(forms.ModelForm):
    class Meta:
        model = AutosCreate
        fields = "__all__"
