from django.db import models

# Create your models here.

class Sector(models.Model):
    sectorCod = models.CharField(max_length=15, unique=True)
    sectorDescripcion = models.CharField(max_length= 30)
    sectorNumero = models.IntegerField()
