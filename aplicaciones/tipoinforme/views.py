from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.tipoinforme.models import TipoInforme


def verTipoInforme(request):
    return render(request, 'mantenedores/tipoinforme/verTipoInforme.html')


class tipoInformes(ListView):
    model = TipoInforme
    template_name = 'mantenedores/tipoInforme/tipoInforme.html'