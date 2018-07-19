from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.turno.models import Turno


def verTurno(request):
    return render(request, 'mantenedores/turno/verTurno.html')


class turnos(ListView):
    model = Turno
    template_name = 'mantenedores/turno/turno.html'