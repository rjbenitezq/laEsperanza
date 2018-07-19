from django.db import models



# Create your models here.

class Cargo(models.Model):
    cargoCod = models.CharField(max_length=10, unique=True)
    cargoDescripcion = models.CharField(max_length=25)



class SubCargo(models.Model):
    subCargoCod = models.CharField(max_length= 10, unique= True)
    subCargoDescripcion = models.CharField(max_length=25)
    cargo = models.ForeignKey(Cargo, on_delete= models.PROTECT)
    def __str__(self):
        return self.subCargoDescripcion