from django.db import models

# Create your models here.

class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    conductor = models.OneToOneField("Conductor", null=False, blank=False, on_delete=models.CASCADE)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    year = models.DateField(null=False, blank=False)
    conductor = models.ForeignKey("Conductor", null=False, blank=False, on_delete=models.CASCADE)

################################################################################

class Artista(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}/{self.apellido}/{self.instrumento}"

class Grupo(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    fecha_creacion = models.DateField(blank=False, null=False)
    artistas = models.ManyToManyField("Artista", through="ArtistaGrupo", related_name="grupos")
    def __str__(self):
        return f"{self.nombre}/{self.fecha_creacion}/{self.artistas}"

class ArtistaGrupo(models.Model):
    artista = models.ForeignKey("Artista", on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey("Grupo", on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField(auto_now_add=True)
    agregado_por = models.CharField(max_length=50)

class Album(models.Model):
    grupo = models.ForeignKey("Grupo", null=False, blank=False, related_name="albumes",on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)