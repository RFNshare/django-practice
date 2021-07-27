from .models import *
from django import forms


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = "__all__"


class CatsForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = "__all__"
