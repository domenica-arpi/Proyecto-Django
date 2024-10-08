from django.db import models

from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
    
class Experiencia(models.Model):
    institucion_del_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.institucion_del_curso} - {self.descripcion_curso}"


# Nuevo modelo de Educacion
class Educacion(models.Model):
    titulo = models.CharField(max_length=255)
    institucion = models.CharField(max_length=255)
    anio_inicio = models.IntegerField()
    anio_fin = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"