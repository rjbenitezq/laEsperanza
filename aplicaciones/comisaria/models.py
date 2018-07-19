from django.db import models

# Create your models here.

class Comisaria(models.Model):
    comisariaCod = models.CharField(max_length=10, unique=True)
    comisariaNombre = models.CharField(max_length=50)
    comisariaDireccion = models.CharField(max_length=80)
    comisariaTelef = models.CharField(max_length=20)
    comisariaResponsable = models.CharField(max_length=30)

    def __str__(self):
        return self.comisariaNombre
