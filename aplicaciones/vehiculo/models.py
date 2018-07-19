from django.db import models

from aplicaciones.tipovehiculo.models import TipoVehiculo


# Create your models here.

class Vehiculo(models.Model):
    vehiculoCod = models.CharField(max_length=15, unique=True)
    vehiculoMarca = models.CharField(max_length=30)
    vehiculoModelo = models.CharField(max_length=20)
    vehiculoPlaca = models.CharField(max_length=20, unique=True)
    vehiculoNumero = models.IntegerField(null=True)
    tipovehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)

    def __str__(self):
        return self.vehiculoPlaca
