from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.template.loader import render_to_string

from aplicaciones.incidencia.forms import IncidenciaForm
from aplicaciones.informe.forms import InformeForm
from aplicaciones.informe.models import Informe


def verInforme(request):
    informe = Informe.objects.all()
    context = {
        'informe': informe
    }
    return render(request, 'informes/registroInforme/informe_list.html', context)


def verActividad(request):
    informe = Informe.objects.all()
    context = {
        'informe': informe
    }
    return render(request, 'reportes/actividades/actividad_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            informe = Informe.objects.all()
            data['informe_list'] = render_to_string('informes/registroInforme/informe_list_2.html',
                                                    {'informe': informe})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def informe_create(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
    else:
        form = InformeForm()
    return save_all(request, form, 'informes/registroInforme/informe_create.html')


def informe_update(request, id):
    informe = get_object_or_404(Informe, id=id)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
    else:
        form = InformeForm(instance=informe)
    return save_all(request, form, 'informes/registroInforme/informe_update.html')


def informe_delete(request, id):
    data = dict()
    informe = get_object_or_404(Informe, id=id)
    if request.method == "POST":
        informe.delete()
        data['form_is_valid'] = True
        informe = Informe.objects.all()
        data['informe_list'] = render_to_string('informes/registroInforme/informe_list_2.html',
                                                {'informe': informe})
    else:
        context = {'informe': informe}
        data['html_form'] = render_to_string('informes/registroInforme/informe_delete.html', context, request=request)

    return JsonResponse(data)
