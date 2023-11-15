from django.shortcuts import render
from gestion_internaciones.models import Pacientes
from gestion_internaciones.forms import FormPaciente
# Create your views here.
def listapacientes (request):
    pacientes = Pacientes.objects.all()
    
    context = {
        'pacientes': pacientes,
    }
    
    return render(request, 'pacientes.html', context) 

def agregarpaciente(request):

    formulario = FormPaciente()
    if request.method == 'POST':

        formulario = FormPaciente(request.POST)

        if formulario.is_valid():
            paciente = Pacientes(
                nombre_pac = formulario.cleaned_data['nombre'],
                apellido_pac = formulario.cleaned_data['apellido'],
                dni_pac = formulario.cleaned_data['dni'],
                domicilio_pac = formulario.cleaned_data['domicilio'],
                telefono_pac = formulario.cleaned_data['telefono'],

            )
            paciente.save()

            formulario = FormPaciente()
        
    context = {
        'formulario': formulario,
    }   
    return render(request, 'agregarpaciente.html', context)