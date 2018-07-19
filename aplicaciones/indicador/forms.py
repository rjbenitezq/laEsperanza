from django import forms

from aplicaciones.indicador.models import Indicador


class IndicadorForm(forms.ModelForm):
    """docstring for PersonaForm"""

    class Meta:
        """docstring for Meta:"""
        model = Indicador
        fields = [
            'indicadorCod',
            'indicadorDescripcion',
            'indicadorTipo',
        ]

        labels = {

            'indicadorCod': 'Codigo',
            'indicadorDescripcion': 'Descripción',
            'indicadorTipo': 'Tipo'
        }
        widgets = {

            'indicadorCod': forms.TextInput(attrs={'class': 'form-control'}),
            'indicadorDescripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'indicadorTipo': forms.TextInput(attrs={'class': 'form-control'}),
        }
