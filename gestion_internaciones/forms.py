from django import forms
from gestion_internaciones.models import Pacientes, Drogueria, Internaciones, Obras_Pacientes, Internaciones, Prescripciones, Obras_Sociales, Coseguros
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
        widget= forms.Select(),
        initial='4',
        disabled=True
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

class forminternacion(forms.ModelForm):
    class Meta:
        model = Internaciones
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        pacientes_disponibles = kwargs.pop('pacientes_disponibles', None)
        super(forminternacion, self).__init__(*args, **kwargs)

        if pacientes_disponibles:
            self.fields['paciente_inter'].queryset = pacientes_disponibles



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

class AsignarObraCoseguroForm(forms.ModelForm):
    class Meta:
        model = Obras_Pacientes
        fields = ['obra_social', 'coseguro']

    def __init__(self, *args, **kwargs):
        super(AsignarObraCoseguroForm, self).__init__(*args, **kwargs)

        # Personaliza las opciones para el campo de obra social
        obras_sociales = Obras_Sociales.objects.all()
        self.fields['obra_social'].queryset = obras_sociales

        # Personaliza las opciones para el campo de coseguro
        coseguros = Coseguros.objects.all()
        self.fields['coseguro'].queryset = coseguros
class formprescripcion(forms.ModelForm):
    class Meta:
        model = Prescripciones

        fields='__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'personal_paciente',
            'medicamentos',
            'detalles_de_control',
            
            Submit('submit', 'Guardar')
        )
