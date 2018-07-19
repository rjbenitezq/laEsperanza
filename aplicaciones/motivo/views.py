from aplicaciones.motivo.forms import MotivoForm
from aplicaciones.motivo.models import Motivo

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.template.loader import render_to_string


def verMotivo(request):
    motivo = Motivo.objects.all()
    context = {
        'motivo': motivo
    }
    return render(request, 'informes/motivo/motivo_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            motivo = Motivo.objects.all()
            data['motivo_list'] = render_to_string('informes/motivo/motivo_list_2.html',
                                                   {'motivo': motivo})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def motivo_create(request):
    if request.method == 'POST':
        form = MotivoForm(request.POST)
    else:
        form = MotivoForm()
    return save_all(request, form, 'informes/motivo/motivo_create.html')


def motivo_update(request, id):
    motivo = get_object_or_404(Motivo, id=id)
    if request.method == 'POST':
        form = MotivoForm(request.POST, instance=motivo)
    else:
        form = MotivoForm(instance=motivo)
    return save_all(request, form, 'informes/motivo/motivo_update.html')


def motivo_delete(request, id):
    data = dict()
    motivo = get_object_or_404(Motivo, id=id)
    if request.method == "POST":
        motivo.delete()
        data['form_is_valid'] = True
        motivo = Motivo.objects.all()
        data['motivo_list'] = render_to_string('informes/motivo/motivo_list_2.html', {'motivo': motivo})
    else:
        context = {'motivo': motivo}
        data['html_form'] = render_to_string('informes/motivo/motivo_delete.html', context, request=request)

    return JsonResponse(data)
