from django.db import models


# Create your models here.

class Turno(models.Model):
    turnoCod = models.CharField(max_length=15, unique=True)
    turnoDescripcion = models.CharField(max_length=15)
    turnoHoraInicio = models.TimeField()
    turnoHoraFin = models.TimeField()

    def __str__(self):
        return self.turnoDescripcion