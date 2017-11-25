from django.contrib.admin import widgets
from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = ('nombre', 'descripcion',)
