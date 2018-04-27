from django import forms
from equipos.models import Equipo

class SearchForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipo',]
