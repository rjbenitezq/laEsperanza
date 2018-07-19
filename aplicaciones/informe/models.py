from django.db import models

from aplicaciones.patrullaje.models import Patrullaje
from aplicaciones.tipoinforme.models import TipoInforme
from aplicaciones.personal.models import Personal
from aplicaciones.turno.models import Turno
from aplicaciones.indicador.models import Indicador
from aplicaciones.motivo.models import Motivo
from aplicaciones.vehiculo.models import Vehiculo
from aplicaciones.comisaria.models import Comisaria
from aplicaciones.incidencia.models import Incidencia


# Create your models here.

class Informe(models.Model):
    informeCod = models.CharField(max_length=15, unique=True)
    informeFecha = models.DateField()
    informeAsunto = models.CharField(max_length=50)
    informeObservacion = models.CharField(max_length=150, null=True)
    tipoinforme = models.ForeignKey(TipoInforme, on_delete=models.PROTECT)
    personal = models.ForeignKey(Personal, on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    patrullaje = models.ForeignKey(Patrullaje, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    indicador = models.ForeignKey(Indicador, on_delete=models.PROTECT)
    motivo = models.ForeignKey(Motivo, on_delete=models.PROTECT, null=True)
    comisaria = models.ForeignKey(Comisaria, on_delete=models.PROTECT, null=True)
    incidencia = models.ForeignKey(Incidencia, on_delete=models.PROTECT)
