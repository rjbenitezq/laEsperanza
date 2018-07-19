from django import forms

from aplicaciones.cargo.models import Cargo
from aplicaciones.indicador.models import Indicador
from aplicaciones.informe.models import Informe
from aplicaciones.personal.models import Personal

cargo = Cargo.objects.get(cargoDescripcion="sereno")


class InformeForm(forms.ModelForm):
    """docstring for PersonaForm"""
    personal = Personal.objects.filter(cargo_id=cargo.pk)

    class Meta:
        """docstring for Meta:"""
        model = Informe
        fields = [
            'informeCod',
            'informeFecha',
            'informeAsunto',
            'tipoinforme',
            'personal',
            'turno',
            'patrullaje',
            'vehiculo',
            'indicador',
            'motivo',
            'informeObservacion',
            'comisaria',
            'incidencia',
        ]

        labels = {

            'informeCod': 'Codigo',
            'informeFecha': 'Fecha',
            'informeAsunto': 'Asunto',
            'tipoinforme': 'Tipo de Informe',
            'personal': 'Sereno',
            'turno': 'Turno',
            'patrullaje': 'Patrullaje',
            'vehiculo': 'Vehiculo',
            'indicador': 'Indicadores',
            'motivo': 'Motivo',
            'informeObservacion': 'Observación',
            'comisaria': 'Comisaria',
            'incidencia': 'Incidencia'
        }
        widgets = {

            'informeCod': forms.TextInput(attrs={'class': 'form-control'}),
            'informeFecha': forms.TextInput(attrs={'class': 'form-control'}),
            'informeAsunto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoinforme': forms.Select(attrs={'class': 'form-control'}),
            'personal': forms.Select(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
            'patrullaje': forms.Select(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'informeObservacion': forms.TextInput(attrs={'class': 'form-control'}),
            'comisaria': forms.Select(attrs={'class': 'form-control'}),
            'incidencia': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(InformeForm, self).__init__(*args, **kwargs)
        self.fields['comisaria'].required = False
