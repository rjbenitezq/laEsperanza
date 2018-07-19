from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from aplicaciones.patrullaje.models import Patrullaje


def verPatrullaje(request):
    return render(request, 'mantenedores/patrullaje/verPatrullajje.html')


class patrullajes(ListView):
    model = Patrullaje
    template_name = 'mantenedores/patrullaje/patrullaje.html'