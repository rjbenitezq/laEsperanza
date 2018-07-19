from django.db import models


# Create your models here.

class Patrullaje(models.Model):
    patrullajeCod = models.CharField(max_length=15, unique=True)
    patrullajeDescripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.patrullajeDescripcion
