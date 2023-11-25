from django import forms
from gestion_internaciones.models import Pacientes, Drogueria, Obras_Pacientes, Internaciones
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
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

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]

class formdroga(forms.ModelForm):
    class Meta:
        model = Drogueria

        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'nombre_drog',
            'stock_drog',
            Submit('submit', 'Guardar')
        )

class asignarhab(forms.ModelForm):

    class Meta:
        model = Internaciones

        fields='__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'paciente_inter',
            'habitacion_inter',
            'fecha_ingreso',
            'hora_ingreso',
            'fecha_egreso',
            'hora_egreso',
            
            Submit('submit', 'Guardar')
        )

class asignarObra(forms.ModelForm):

    class Meta:
        model = Obras_Pacientes

        fields='__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'paciente',
            'obra_social',
            'coseguro',
            
            Submit('submit', 'Guardar')
        )