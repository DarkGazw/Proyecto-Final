from django.shortcuts import render, redirect
from gestion_internaciones.models import Pacientes, Personal, Drogueria, Internaciones
from gestion_internaciones.forms import FormPaciente, formdroga, forminternacion
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
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

def register(request):
    if request.method== 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationForm})
    
    if request.method== 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user= form.save(commit=False)
            user.save()

            user=authenticate(
                username= form.cleaned_data['username'],
                password= form.cleaned_data['password1']
            )

            login(request, user)

            return redirect('home')
        
        else:
            return render(request, 'registration/register.html', {'form': form})
        

def listaPersonal(request):
    personal = Personal.objects.all()

    context={
        'personal': personal
    }

    return render(request, 'listapersonal.html', context)


def home(request):
    context = {}

    return render(request, 'home/home.html', context)

def agregardroga(request):
    formulario = formdroga()
    if request.method== 'POST':
        formulario = formdroga(request.POST)
        if formulario.is_valid(): 
            formulario.save()
            formulario = formdroga()
                
    context={
        'formulario': formulario
    }
    return render(request, 'agregardroga.html', context)

def listadroga(request):
    drogueria = Drogueria.objects.all()

    context={
        'drogueria': drogueria
    }

    return render(request, 'listadrogueria.html', context)


def listainternaciones(request):
    internaciones = Internaciones.objects.all()

    context={
        'internaciones' : internaciones

    }
    return render(request, 'internaciones.html', context)

def agregarinternacion(request):
    formulario = forminternacion()
    if request.method == 'POST':
        formulario = forminternacion(request.POST)
        if formulario.is_valid(): 
            formulario.save()
            formulario = forminternacion()
                
    context={
        'formulario': formulario
    }
    return render(request, 'agregarinternacion.html', context)