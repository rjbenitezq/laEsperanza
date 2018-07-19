from django import forms

from aplicaciones.incidencia.models import Incidencia
from aplicaciones.indicador.models import Indicador


class IncidenciaForm(forms.ModelForm):
    """docstring for PersonaForm"""

    class Meta:
        """docstring for Meta:"""
        model = Incidencia
        fields = [
            'incidenciaCod',
            'incidenciaDescripcion',
            'incidenciaTraslado',
            'incidenciaMasculino',
            'incidenciaFemenino',
            'incidenciaHeridos',
            'incidenciaMuertos',
        ]

        labels = {
            'incidenciaCod': 'Codigo de Incidencia',
            'incidenciaDescripcion': 'Descripción Incidencia',
            'incidenciaTraslado': 'Translado',
            'incidenciaMasculino': 'Masculino',
            'incidenciaFemenino': 'Femenino',
            'incidenciaHeridos': 'Heridos',
            'incidenciaMuertos': 'Muertos',
        }
        widgets = {
            'incidenciaCod': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaDescripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaTraslado': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaMasculino': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaFemenino': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaHeridos': forms.TextInput(attrs={'class': 'form-control'}),
            'incidenciaMuertos': forms.TextInput(attrs={'class': 'form-control'}),
        }
