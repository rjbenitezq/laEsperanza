from django import forms
from aplicaciones.personal.models import Personal


class PersonalForm(forms.ModelForm):
    """docstring for PersonaForm"""

    class Meta:
        """docstring for Meta:"""
        model = Personal
        fields = [
            'personalApellidos',
            'personalNombres',
            'personalGenero',
            'personalDni',
            'personalTelefono',
            'personalEmail',
            'personalDomicilio',
            'personalFechaNac',
            'cargo',
            'turno',
        ]

        labels = {

            'personalApellidos': 'Apellidos',
            'personalNombres': 'Nombres',
            'personalGenero': 'Sexo',
            'personalDni': 'Dni',
            'personalTelefono': 'Telefono',
            'personalEmail': 'Email',
            'personalDomicilio': 'Domicilio',
            'personalFechaNac': 'Fecha de Nacimiento',
            'cargo': 'Cargo',
            'turno': 'Turno',
        }
        widgets = {

            'personalApellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'personalNombres': forms.TextInput(attrs={'class': 'form-control'}),
            'personalGenero': forms.TextInput(attrs={'class': 'form-control'}),
            'personalDni': forms.TextInput(attrs={'class': 'form-control'}),
            'personalTelefono': forms.TextInput(attrs={'class': 'form-control'}),
            'personalEmail': forms.TextInput(attrs={'class': 'form-control'}),
            'personalDomicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'personalFechaNac': forms.TextInput(attrs={'class': 'form-control pull-right date'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
        }
