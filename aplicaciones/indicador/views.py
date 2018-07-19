import random

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.template.loader import render_to_string

from aplicaciones.indicador.forms import IndicadorForm
from aplicaciones.indicador.models import Indicador


def verIndicador(request):
    indicador = Indicador.objects.all()
    context = {
        'indicador': indicador
    }
    return render(request, 'informes/indicador/indicador_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            indicador = Indicador.objects.all()
            data['indicador_list'] = render_to_string('informes/indicador/indicador_list_2.html',
                                                      {'indicador': indicador})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def indicador_create(request):
    if request.method == 'POST':
        form = IndicadorForm(request.POST)
    else:
        form = IndicadorForm()
    return save_all(request, form, 'informes/indicador/indicador_create.html')


def indicador_update(request, id):
    indicador = get_object_or_404(Indicador, id=id)
    if request.method == 'POST':
        form = IndicadorForm(request.POST, instance=indicador)
    else:
        form = IndicadorForm(instance=indicador)
    return save_all(request, form, 'informes/indicador/indicador_update.html')


def indicador_delete(request, id):
    data = dict()
    indicador = get_object_or_404(Indicador, id=id)
    if request.method == "POST":
        indicador.delete()
        data['form_is_valid'] = True
        indicador = Indicador.objects.all()
        data['indicador_list'] = render_to_string('informes/indicador/indicador_list_2.html', {'indicador': indicador})
    else:
        context = {'indicador': indicador}
        data['html_form'] = render_to_string('informes/indicador/indicador_delete.html', context, request=request)

    return JsonResponse(data)
