from django.db import models

# Create your models here.
from aplicaciones.sector.models import Sector


class Subsector(models.Model):
    subsectorCod = models.CharField(max_length=15, unique=True)
    subsectorDescripcion = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)