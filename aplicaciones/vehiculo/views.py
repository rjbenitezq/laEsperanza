from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.vehiculo.models import Vehiculo


def verVehiculo(request):
    return render(request, 'mantenedores/vehiculo/verVehiculo.html')


class vehiculos(ListView):
    model = Vehiculo
    template_name = 'mantenedores/vehiculo/vehiculo.html'


