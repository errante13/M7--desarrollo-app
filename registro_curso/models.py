from django.db import models

# Create your models here.
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()
    Profesor_id = models.ManyToManyField(Profesor)
    
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    depto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=10, null=False)
    ciudad = models.CharField(max_length=10, null=False)
    region = models.CharField(max_length=10, null=False)
    estudiante_id = models.OneToOneField("Estudiante", verbose_name=("estudiantes"), on_delete=models.CASCADE)    
    