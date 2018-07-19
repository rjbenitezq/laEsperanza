from django import forms

from aplicaciones.motivo.models import Motivo


class MotivoForm(forms.ModelForm):
    """docstring for PersonaForm"""

    class Meta:
        """docstring for Meta:"""
        model = Motivo
        fields = [
            'motivoCod',
            'motivoDescripcion',
            'indicador',
        ]

        labels = {

            'motivoCod': 'Codigo',
            'motivoDescripcion': 'Descripción del motivo',
            'indicador': 'indicador',
        }
        widgets = {
            'motivoCod': forms.TextInput(attrs={'class': 'form-control'}),
            'motivoDescripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'indicador': forms.Select(attrs={'class': 'form-control'}),
        }
