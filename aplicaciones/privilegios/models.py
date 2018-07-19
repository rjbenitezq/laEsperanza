from django.db import models

# Create your models here.

class Opcion(models.Model):
    opcionDescripcion = models.CharField(max_length=20)
    opcionRecurso = models.CharField(max_length=100)
    NAPCodigo = models.CharField(max_length=1)
    NOPEstado = models.CharField(max_length=1)
    NOPDependencia = models.IntegerField()
    opcionIcono = models.CharField(max_length=70)

    def __str__(self):
        return '{}'.format(self.opcionDescripcion)