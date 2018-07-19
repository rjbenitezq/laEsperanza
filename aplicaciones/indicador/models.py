from django.db import models


# Create your models here.

class Indicador(models.Model):
    indicadorCod = models.CharField(max_length=15, unique=True)
    indicadorDescripcion = models.CharField(max_length=50)
    indicadorTipo = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.indicadorDescripcion
