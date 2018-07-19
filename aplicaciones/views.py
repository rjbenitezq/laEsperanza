from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from aplicaciones.personal.models import Personal


@method_decorator(csrf_exempt, name='dispatch')
def panelPrincipal(request):
    a = request.user.id
    personal = Personal.objects.get(user_id=a)
    user = User.objects.get(id=a)
    contexto = {'personal': personal, 'user': user}
    return render(request, 'index.html', contexto)


@method_decorator(csrf_exempt, name='dispatch')
def menuOpciones(request):
    a = request.user.id
    personal = Personal.objects.get(user_id=a)
    personal2 = Personal.objects.get(user_id=a)
    contexto = {'personal': personal, 'personal2': personal2}
    return render(request, 'menu.html', contexto)
