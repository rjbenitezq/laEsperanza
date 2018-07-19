from django.shortcuts import render

# Create your views here.
from aplicaciones.efectivopol.models import EfectivoPol
from django.views.generic import ListView


def verEfectivoPol(request):
    return render(request, 'mantenedores/efectivopol/verEfectivoPol.html')


class efectivoPol(ListView):
    model = EfectivoPol
    template_name = 'mantenedores/efectivopol/efectivoPol.html'

