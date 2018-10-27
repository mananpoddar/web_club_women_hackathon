from django.db import models
from django import forms
from todolist.models import liste

class input(forms.ModelForm):
    class Meta:
        model = liste
        fields= '__all__'
