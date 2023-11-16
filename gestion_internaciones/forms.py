from django import forms
from gestion_internaciones.models import Pacientes
class FormPaciente(forms.Form):

    class Meta:
        model = Pacientes
        fields = ['estado_pac']

    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre del paciente'
            }
        )
    )

    apellido = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese apellido del paciente'
            }
        )
    )

    dni = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese dni del paciente'
            }
        )
    )

    domicilio = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese domicilio del paciente'
            }
        )
    )

    telefono = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese telefono del paciente'
            }
        )
    )
    estado = forms.ChoiceField(
        choices=Pacientes.estados_choices,
        widget= forms.Select()
    )
    
    
class formdroga(forms.Form):
        
        Nombre = forms.CharField(
            max_length=20, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la droga'}))
        
        Stock = forms.IntegerField(
            widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el stock de la droga'})
        )