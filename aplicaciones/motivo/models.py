from django.db import models

from aplicaciones.indicador.models import Indicador


# Create your models here.

class Motivo(models.Model):
    motivoCod = models.CharField(max_length=15, unique=True)
    motivoDescripcion = models.CharField(max_length=50)
    indicador = models.ForeignKey(Indicador, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivoDescripcion
