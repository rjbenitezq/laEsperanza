from django.db import models

# Create your models here.

from aplicaciones.comisaria.models import Comisaria


class EfectivoPol(models.Model):
    efectivopolCod = models.CharField(max_length=15, unique=True)
    efectivopolApellidos = models.CharField(max_length=30)
    efectivopolNombres = models.CharField(max_length=30)
    efectivopolDni = models.CharField(max_length=30)
    comisaria = models.ForeignKey(Comisaria, on_delete=models.PROTECT)