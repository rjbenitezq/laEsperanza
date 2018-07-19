from django.db import models


# Create your models here.

class Incidencia(models.Model):
    incidenciaCod = models.CharField(max_length=15, null=True)
    incidenciaDescripcion = models.CharField(max_length=80, null=True)
    incidenciaTraslado = models.CharField(max_length=2, null=True)
    incidenciaMasculino = models.IntegerField(null=True)
    incidenciaFemenino = models.IntegerField(null=True)
    incidenciaHeridos = models.IntegerField(null=True)
    incidenciaMuertos = models.IntegerField()

    def __str__(self):
        return self.incidenciaDescripcion
