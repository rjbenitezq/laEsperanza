from django.shortcuts import render

# Create your views here.
from aplicaciones.cargo.models import Cargo
from django.views.generic import ListView

def verCargo(request):
    return render(request, 'mantenedores/cargo/verCargo.html')


class cargos(ListView):
    model = Cargo
    template_name = 'mantenedores/cargo/cargo.html'

def CargoCreate_ajax(request):
    if request.method == 'POST':
        # request.is_ajax() and
        return render(request, 'mantenedores/cargo/verCargo.html')
    else:
        # formulario = PersonalForm()
        return render(request, 'mantenedores/cargo/createCargo.html')