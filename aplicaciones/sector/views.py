from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.sector.models import Sector


def verSector(request):
    return render(request, 'mantenedores/sector/verSector.html')


class sectores(ListView):
    model = Sector
    template_name = 'mantenedores/sector/sector.html'