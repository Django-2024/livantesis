from django.db import models

# Create your models here.

# Nomencladores de la region
class Pais_region(models.Model):
	paisregion = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.paisregion

class Provincia(models.Model):
    nom_provincia = models.CharField( max_length = 256, blank=True, null=True)
    codigo_provincia = models.CharField( max_length = 3, blank=True, null=True)
    paisProvinciaPertenece = models.ForeignKey(Pais_region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return '%s' % self.nom_provincia

class Municipio(models.Model):
    nom_municipio = models.CharField( max_length = 256, blank=True, null=True)
    codigo_municipio = models.CharField( max_length = 3, blank=True, null=True)
    provinciaMunicipioPertenece = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return '%s' % self.nom_municipio

# Programa y proyectos
class Programa(models.Model):
    nombrePrograma = models.CharField(max_length=250, blank=True, null=True)
    logoPrograma = models.ImageField(upload_to='Logo del Programa/', blank=True, null=True)

    def __str__(self):
    	return '%s' % self.nombrePrograma

class Proyecto(models.Model):
    nombreProyecto = models.CharField(verbose_name='Nombre del Proyecto', max_length=200)
    descripcionProyecto = models.TextField(max_length=4000, blank=True, null=True)
    logoProyecto = models.ImageField(upload_to='Logo del Proyecto/', blank=True, null=True)
    pertenecePrograma = models.ForeignKey(Programa,  on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombreProyecto

# Entidad Beneficiada
class TipoDeEntidadBeneficiada(models.Model):
	tipoDeEntidadBeneficiada = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.tipoDeEntidadBeneficiada

class EntidadBeneficiada(models.Model):    
    entidadBeneficiada = models.CharField(max_length=200)
    tipoEntidad = models.ForeignKey(TipoDeEntidadBeneficiada, on_delete=models.SET_NULL, null=True)
    municipio_entidadBenef = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    codigoEntidadBeneficiada = models.CharField( max_length = 256, blank=True, null=True)

    def __str__(self):
    	return '%s' % self.tipoEntidad + ' ' + self.entidadBeneficiada

# Trabajadores y datos generales
class Sexo(models.Model):
	Sexo = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.Sexo

class FormacionAcademica(models.Model):
    tipoFormacionAcademica = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.tipoFormacionAcademica

class RolesProyecto(models.Model):
    rolesProyecto = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.rolesProyecto

class TipoDeTrabajador(models.Model):
	tipoDeTrabajador = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.tipoDeTrabajador


	def __str__(self):
		return '%s' % self.tipoDeTrabajador

class Trabajadores(models.Model):
    nombreTrabajador = models.CharField(max_length=200)
    carneID = models.CharField(max_length = 11, blank=True, null=True)
    sexo = models.ForeignKey(Sexo, on_delete = models.SET_NULL, null=True)
    edad = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length = 300, blank=True, null=True)
    formacionAcademica = models.ForeignKey(FormacionAcademica, on_delete = models.SET_NULL, null=True)
    tipoTrabajador = models.ForeignKey(TipoDeTrabajador, on_delete = models.SET_NULL, null=True)
    rolProyecto = models.ForeignKey(RolesProyecto, on_delete = models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='Imagenes de Beneficiarios/', blank=True, null=True)
    
    def __str__(self):
    	return '%s' % self.nombreTrabajador + ' que ocupa el cargo de ' + self.rolProyecto.rolesProyecto

# Cadena de valor
class TipoCadenaValor(models.Model):
    tipoCadenaValor = models.CharField(max_length = 200)
    
    def __str__(self):
    	return '%s' % self.tipoCadenaValor

class EslabonCadena(models.Model):
    eslabonCadena = models.CharField(max_length=200)
   
    def __str__(self):
        return '%s' % self.eslabonCadena

class CadenaDeValor(models.Model):
    nombreProducto = models.CharField(max_length=200)
    tipoDeCadena = models.ForeignKey(TipoCadenaValor, on_delete = models.CASCADE)

    def __str__(self):
    	return '%s' % self.tipoDeCadena + ' con el producto ' + self.nombreProducto

# Recursos
class Proveedor(models.Model):
	proveedor = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.proveedor

class TipoRecurso(models.Model):
    tiporecurso = models.CharField(max_length=200)

    def __str__(self):
    	return '%s' % self.tiporecurso

class Recursos(models.Model):
    nombreRecurso = models.CharField(verbose_name = 'Recurso', max_length=200)
    descripcionRecurso = models.TextField(verbose_name = 'Descripción', max_length=5000)
    tipoRecurso = models.ForeignKey(TipoRecurso, verbose_name = 'Tipo de Recurso', on_delete = models.SET_NULL, null=True)
    codigoRecursoInv = models.IntegerField(verbose_name = 'Código del Recurso', blank = True, null = True)
    proveedorRecurso = models.ForeignKey(Proveedor, on_delete = models.SET_NULL, null=True)
    puestaEnMarcha = models.BooleanField(default = False)


    #?  preguntar si cuando se añade un recurso se pone la cantidad
    def __str__(self):
        return '%s' % self.nombreRecurso

# Factura
class ClientesFactura(models.Model):
    nombre_cliente = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.nombre_cliente

class Factura(models.Model):
    imagen_factura = models.ImageField(upload_to='facturas/%Y/%m/%d/')
    fechaEmision = models.DateField(blank=True, null=True)
    codigoRecursoFactura = models.CharField(max_length = 250)
    numeroFactura = models.CharField(max_length=250)
    organismoEmiteFactura = models.CharField(max_length=250)
    clienteFactura = models.ForeignKey(ClientesFactura, on_delete=models.SET_NULL, null=True)
    recursoFacturado = models.ForeignKey(Recursos, on_delete=models.SET_NULL, null=True)
    cantidadRecursoFacturado = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=5)
    importeTotal = models.DecimalField(max_digits=10, decimal_places=5)
    recargoComercial = models.DecimalField(max_digits=10, decimal_places=5)
    comentario = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.numeroFactura

# Contratos
class Contratos(models.Model):
    contratos = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.contratos

# Distribucion
class Distribucion(models.Model):
    nombreDistribucion = models.CharField(max_length=200)
    contrato = models.ForeignKey(Contratos, models.SET_NULL, null=True)
    montoDistribucion = models.DecimalField(max_digits=10, decimal_places=5)
    descripcionRecursoDistr = models.CharField(max_length=300)
    clienteDistrib = models.ForeignKey(ClientesFactura, models.SET_NULL, null=True)
    entidadRecibeRecurso = models.ForeignKey(EntidadBeneficiada,  models.SET_NULL, null=True)
    municipio_distrib = models.ForeignKey(Municipio, models.SET_NULL, null=True)
    cantidadRecursoDistribuido = models.IntegerField()
    cadenaQueApoyaDistr = models.ForeignKey(TipoCadenaValor, models.SET_NULL, null=True)
    autorizaDistribucion = models.ForeignKey(Trabajadores, models.SET_NULL, null=True)

# Beneficiarios
class Beneficiario(models.Model):
    nombreBeneficiario = models.CharField(verbose_name = 'Nombre del(a) Beneficiario(a)', max_length=200)
    rolProyecto = models.ManyToManyField(RolesProyecto, blank=True)
    carneID = models.CharField(max_length = 11, blank=True, null=True)
    sexo = models.ForeignKey(Sexo, on_delete = models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='Imagenes de Beneficiarios/', blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length = 300, blank=True, null=True)
    entidadQuePertenece = models.ForeignKey(EntidadBeneficiada, verbose_name= 'Entidad que pertenece', on_delete = models.SET_NULL, null=True)
    cadenaQueTributa = models.ManyToManyField(CadenaDeValor, blank=True)
    eslabonParticipa = models.ManyToManyField(EslabonCadena, blank=True)
    recursoRecibido = models.ManyToManyField(Recursos, blank=True)

    def display_cadenaQueTributa(self):
        return ', '.join([ cadenaQueTributa.tipoDeCadena.tipoCadenaValor for cadenaQueTributa in self.cadenaQueTributa.all()[:3] ])


    display_cadenaQueTributa.short_description = 'Cadena que tributa'


    def display_eslabonParticipa(self):
        return ', '.join([ eslabonParticipa.eslabonCadena for eslabonParticipa in self.eslabonParticipa.all()[:5] ])


    display_eslabonParticipa.short_description = 'Eslabón en el que participa'

    def __str__(self):
    	return '%s' % self.nombreBeneficiario + ' de la ' + self.entidadQuePertenece.tipoEntidad.tipoDeEntidadBeneficiada + ' ' + self.entidadQuePertenece.entidadBeneficiada

# Experiencias y capacitaciones
class TipoDeCapacitacion(models.Model):
	tipoDeCapacitacion = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.tipoDeCapacitacion

class TipoDeExperiencia(models.Model):
	tipoDeExperiencia = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % self.tipoDeExperiencia

class ExperienciasObtenidas(models.Model):
    nombreExperiencia = models.CharField(max_length=200)
    descripcionExperiencia = models.TextField(max_length=4000)
    evidencia = models.ImageField(upload_to='Imagenes de Experiencias/', blank=True, null=True)
    tipoExperiencia = models.ForeignKey(TipoDeExperiencia,  on_delete=models.SET_NULL, null=True)
    beneficiarioExperimentado = models.ManyToManyField(Beneficiario, blank=True)
    trabajadorExperimentado = models.ManyToManyField(Trabajadores, blank=True)
    

    def __str__(self):
        return '%s' % self.nombreExperiencia

class Capacitaciones(models.Model):
    temaDeCapacitacion = models.CharField(verbose_name = 'Tema de Capacitación',max_length=200)
    descripcionCapacitacion = models.TextField(verbose_name = 'Breve descripción de la capacitación', max_length=4000)
    fechaCapacitacion = models.DateField(verbose_name = 'Fecha de la Capacitación', blank = True, null = True)
    evidencia = models.ImageField(upload_to='Imagenes de Capacitaciones/%Y/%m/%d/', blank=True, null=True)
    tipoCapacitacion = models.ManyToManyField(TipoDeCapacitacion, blank=True)
    registroAsistencia = models.ImageField(upload_to='Imagenes de Asistencia a Capacitaciones/%Y/%m/%d/', blank=True, null=True)
    proyectoQueApoya = models.ManyToManyField(Proyecto, verbose_name = 'Proyecto que Apoya', blank=True)
    beneficiarioCapacitado = models.ManyToManyField(Beneficiario, blank=True)
    trabajadorCapacitado = models.ManyToManyField(Trabajadores, blank=True)

    def display_proyectoQueApoya(self):
        return ', '.join([ proyectoQueApoya.nombreProyecto for proyectoQueApoya in self.proyectoQueApoya.all()[:3] ])


    display_proyectoQueApoya.short_description = 'Proyectos que intervienen'

    def __str__(self):
        return '%s' % self.temaDeCapacitacion

#class RecursoDemandado(models.Model): averiguar
