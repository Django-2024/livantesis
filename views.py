from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import formulario_Municipio
from trabajadores.models import * 
from trabajadores.forms import formulario_Municipio
import os
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal  # Asegúrate de importar Decimal
from django.contrib import messages  # Para usar mensajes flash
from django.core.exceptions import ObjectDoesNotExist

# Para el informe (Reporte) Excel
import pandas as pd
import json
import logging
from django.utils import timezone
from openpyxl import Workbook  # Para generar el informe en excel



# Create your views here.

# Portada
def portada(request):
    
    return render(request, 'layouts/portada.html')


###
# CRUD Nom_Municipio
###

def listar_municipio(request):
    municipio = Municipio.objects.all()
    data = { 
        'municipio': municipio,
        
    }
   
    return render(request, 'nomencladores/listar_municipio.html', data)

def crear_municipios(request):
    formulario = formulario_Municipio(request.POST)
    print(formulario)
    print('aqui')
    return render(request, 'nomencladores/form_municipio.html', {'formulario': formulario})




#def editar_municipio(request, id):

    






