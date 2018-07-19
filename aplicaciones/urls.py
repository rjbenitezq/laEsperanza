from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from aplicaciones.cargo.views import verCargo, cargos, CargoCreate_ajax
from aplicaciones.comisaria.views import verComisaria, comisarias
from aplicaciones.motivo.views import *
from aplicaciones.personal.views import verPersonal, personales, PersonalCreate_ajax
from aplicaciones.views import panelPrincipal
from aplicaciones.indicador.views import *
from aplicaciones.informe.views import *
from aplicaciones.incidencia.views import *

urlpatterns = [
    url(r'^panelPrincipal$', panelPrincipal, name="panelPrincipal"),

    url(r'^Personal$', verPersonal, name='verPersonal'),
    url(r'^Personales$', personales.as_view(), name='Personales'),
    url(r'^PersonalCreate$', PersonalCreate_ajax, name='PersonalCreate'),

    url(r'^Actividad/$', csrf_exempt(verActividad), name='verActividad'),
    url(r'^Informe/$', csrf_exempt(verInforme), name='verInforme'),
    url(r'^Informe/create$', csrf_exempt(informe_create), name='informe_create'),
    url(r'^Informe/(?P<id>\d+)/update$', csrf_exempt(informe_update), name='informe_update'),
    url(r'^Informe/(?P<id>\d+)/delete$', csrf_exempt(informe_delete), name='informe_delete'),

    url(r'^Incidencia/$', csrf_exempt(verIncidencias), name='verIncidencia'),

    url(r'^Indicador/$', csrf_exempt(verIndicador), name='verIndicador'),
    url(r'^Indicador/create$', csrf_exempt(indicador_create), name='indicador_create'),
    url(r'^Indicador/(?P<id>\d+)/update$', csrf_exempt(indicador_update), name='indicador_update'),
    url(r'^Indicador/(?P<id>\d+)/delete$', csrf_exempt(indicador_delete), name='indicador_delete'),

    url(r'^Motivo/$', csrf_exempt(verMotivo), name='verIndicador'),
    url(r'^Motivo/create$', csrf_exempt(motivo_create), name='motivo_create'),
    url(r'^Motivo/(?P<id>\d+)/update$', csrf_exempt(motivo_update), name='motivo_update'),
    url(r'^Motivo/(?P<id>\d+)/delete$', csrf_exempt(motivo_delete), name='motivo_delete'),

    url(r'^Cargo$', verCargo, name='verCargo'),
    url(r'^Cargos$', cargos.as_view(), name='Cargos'),
    url(r'^CargoCreate$', CargoCreate_ajax, name='CargoCreate'),

    url(r'^Comisaria$', verComisaria, name='verComisaria'),
    url(r'^Comisarias$', comisarias.as_view(), name='Comisarias')
]
