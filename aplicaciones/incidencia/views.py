from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.incidencia.models import Incidencia


def verIncidencias(request):
    incidencia = Incidencia.objects.all()
    context = {
        'incidencia': incidencia
    }
    return render(request, 'reportes/incidencias/incidencia_list.html', context)
