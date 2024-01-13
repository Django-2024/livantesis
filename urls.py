from django.urls import path
from . import views



urlpatterns = [
    path('', views.listar_municipio),
    path('portada/', views.portada, name="portada"),
    path('crear_municipios/', views.crear_municipios, name="crear_municipios"),
    path('listar_municipio/', views.listar_municipio, name="listar_municipio"),
    #path('index3/', views.index, name="index3"),
    
]