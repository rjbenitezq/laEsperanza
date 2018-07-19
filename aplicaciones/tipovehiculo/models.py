from django.db import models

# Create your models here.

class TipoVehiculo(models.Model):
    tipovehiculoCod = models.CharField(max_length=15, unique=True)
    tipovehiculoNombre = models.CharField(max_length=40)