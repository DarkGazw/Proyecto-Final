from django.shortcuts import render
from gestion_internaciones.models import Pacientes, Drogueria, Personal
from gestion_internaciones.forms import FormPaciente, formdroga
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
                estado_pac = formulario.cleaned_data['estado'],

            )
            paciente.save()

            formulario = FormPaciente()
        
    context = {
        'formulario': formulario,
    }   
    return render(request, 'agregarpaciente.html', context)


def listadrogueria(request):
    listadrogueria = Drogueria.objects.all()
    
    context = {
        
        'drogueria' : listadrogueria,
        
    }
    return render(request, 'listadrogueria.html', context)

def agregardroga(request):
    formulario = formdroga()
    if request.method== 'POST':
            formulario = formdroga(request.POST)
            if formulario.is_valid(): 
                droga = Drogueria(
                    nombre_drog = formulario.cleaned_data['Nombre'],
                    stock_drog = formulario.cleaned_data['Stock'],
                )
                droga.save()
        
                formulario = formdroga()
                
    context={
        'formulario': formulario
    }
    return render(request, 'agregardroga.html', context)

def listaPersonal(request):
    personal = Personal.objects.all()

    context={
        'personal': personal
    }

    return render(request, 'listapersonal.html', context)