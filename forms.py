from .models import Municipio
from django.forms import *
from django import forms

class formulario_Municipio(forms.Form):
    nom_municipio = forms.CharField(label="Municipios", max_length=200)
    codigo_municipio = forms.CharField(label='Código del municipio', max_length=200)
    provinciaMunicipioPertenece = forms.ChoiceField(label='Provincia')
		
