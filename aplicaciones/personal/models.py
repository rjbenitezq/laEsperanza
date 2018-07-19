from django.contrib.auth.models import User
from django.db import models

from aplicaciones.cargo.models import Cargo, SubCargo
from aplicaciones.privilegios.models import Opcion
from aplicaciones.turno.models import Turno


class Personal(models.Model):
    personalCod = models.CharField(max_length=15, unique=True)
    personalApellidos = models.CharField(max_length=60)
    personalNombres = models.CharField(max_length=60)
    personalGenero = models.CharField(max_length=15)
    personalDni = models.CharField(max_length=8, unique=True)
    personalTelefono = models.CharField(max_length=15)
    personalCelular = models.CharField(max_length=15)
    personalEmail = models.EmailField(max_length=50, null=True)
    personalDomicilio = models.CharField(max_length=80)
    personalFechaNac = models.DateField()
    personalEstado = models.CharField(max_length=1)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    subCargo = models.ForeignKey(SubCargo, models.PROTECT, null=True)
    descripcionLIC = models.CharField(max_length=9, null=True)
    categoricaLIC = models.CharField(max_length=5, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    opcion = models.ManyToManyField(Opcion, blank=True)

    def __str__(self):
        return self.personalApellidos
