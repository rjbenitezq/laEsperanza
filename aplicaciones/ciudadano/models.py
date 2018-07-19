from django.db import models

# Create your models here.

class Ciudadano(models.Model):
    ciudadanoCod =models.CharField(max_length=15, unique=True)
    ciudadanoNombres = models.CharField(max_length=80)
    ciudadanoDni = models.CharField(max_length=8)
    ciudadanoEdad = models.IntegerField()