from django import forms

class FormPaciente(forms.Form):
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