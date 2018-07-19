from django.db import models


# Create your models here.

class TipoInforme(models.Model):
    tipoinformeCod = models.CharField(max_length=15, unique=True)
    tipoinformeDescripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.tipoinformeDescripcion
