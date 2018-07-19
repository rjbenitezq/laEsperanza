from django.shortcuts import render

# Create your views here.
from aplicaciones.comisaria.models import Comisaria
from django.views.generic import ListView


def verComisaria(request):
    return render(request, 'mantenedores/comisaria/verComisaria.html')


class comisarias(ListView):
    model = Comisaria
    template_name = 'mantenedores/comisaria/comisaria.html'


