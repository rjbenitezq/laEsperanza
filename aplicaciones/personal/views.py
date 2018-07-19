from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from aplicaciones.cargo.models import Cargo, SubCargo
from aplicaciones.personal.forms import PersonalForm
from aplicaciones.personal.models import Personal
from aplicaciones.turno.models import Turno


def verPersonal(request):
    return render(request, 'mantenedores/personal/verPersonal.html')


class personales(ListView):
    model = Personal
    template_name = 'mantenedores/personal/personal.html'


# paginate_by = 10
# ordering = ['-id']


def PersonalCreate_ajax(request):
    if request.method == 'POST':
        # request.is_ajax() and
        formulario = PersonalForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        # return render(request, 'mantenedores/personal/verPersonal.html')
    else:
        # formulario = PersonalForm()
        cargo = Cargo.objects.all(),
        subCargo = SubCargo.objects.all(),
        turno = Turno.objects.all(),
        contenedor = {'cargo': cargo, 'subCargo': subCargo, 'turno': turno}
        return render(request, 'mantenedores/personal/createPersonal.html', contenedor)
