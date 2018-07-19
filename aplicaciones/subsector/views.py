from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.subsector.models import Subsector


def verSubSector(request):
    return render(request, 'mantenedores/subsector/verSubSector.html')


class subsectores(ListView):
    model = Subsector
    template_name = 'mantenedores/subsector/subSector.html'