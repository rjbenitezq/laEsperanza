from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.tipovehiculo.models import TipoVehiculo


def verTipoVehiculo(request):
    return render(request, 'mantenedores/tipovehiculo/verTipoVehiculo.html')


class tipoVehiculos(ListView):
    model = TipoVehiculo
    template_name = 'mantenedores/tipovehiculo/tipoVehiculo.html'