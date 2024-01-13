from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nombreBeneficiario', 'entidadQuePertenece', 'display_cadenaQueTributa', 'display_eslabonParticipa')

@admin.register(RolesProyecto)
class RolesProyectoAdmin(admin.ModelAdmin):
    pass

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoDeEntidadBeneficiada)
class TipoDeEntidadBeneficiadaAdmin(admin.ModelAdmin):
    pass

@admin.register(EntidadBeneficiada)
class EntidadBeneficiadaAdmin(admin.ModelAdmin):
    pass

@admin.register(CadenaDeValor)
class CadenaDeValorAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoCadenaValor)
class TipoCadenaValorAdmin(admin.ModelAdmin):
    pass

@admin.register(Pais_region)
class Pais_regionAdmin(admin.ModelAdmin):
    pass

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    pass

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    pass

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoDeCapacitacion)
class TipoDeCapacitacionAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoDeExperiencia)
class TipoDeExperienciaAdmin(admin.ModelAdmin):
    pass

@admin.register(ExperienciasObtenidas)
class ExperienciasObtenidasAdmin(admin.ModelAdmin):
    pass

@admin.register(FormacionAcademica)
class FormacionAcademicaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoDeTrabajador)
class TipoDeTrabajadorAdmin(admin.ModelAdmin):
    pass

@admin.register(Trabajadores)
class TrabajadoresAdmin(admin.ModelAdmin):
    pass

@admin.register(EslabonCadena)
class EslabonCadenaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoRecurso)
class TipoRecursoAdmin(admin.ModelAdmin):
    pass


@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nombreRecurso', 'descripcionRecurso', 'codigoRecursoInv')


@admin.register(ClientesFactura)
class ClientesFacturaAdmin(admin.ModelAdmin):
    pass


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Distribucion)
class DistribucionAdmin(admin.ModelAdmin):
    pass


@admin.register(Capacitaciones)
class CapacitacionesAdmin(admin.ModelAdmin):
    list_display = ('temaDeCapacitacion', 'descripcionCapacitacion', 'fechaCapacitacion', 'display_proyectoQueApoya')

