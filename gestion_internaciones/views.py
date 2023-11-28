from django.shortcuts import render, redirect
from gestion_internaciones.models import Pacientes, Personal, Drogueria, Internaciones, Obras_Sociales, Coseguros, Obras_Pacientes, Prescripciones, Personal_Paciente
from gestion_internaciones.forms import FormPaciente, formdroga, forminternacion, AsignarObraCoseguroForm,formprescripcion
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
import datetime
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
        
@login_required
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

def agregar_internacion(request):
    # Filtrar los pacientes que no están internados
    pacientes_disponibles = Pacientes.objects.exclude(estado_pac='1')  # Excluir a los pacientes internados

    if request.method == 'POST':
        formulario = forminternacion(request.POST, pacientes_disponibles=pacientes_disponibles)
        if formulario.is_valid():
            internacion = formulario.save(commit=False)

            # Obtén el paciente asociado a la internación
            paciente = internacion.paciente_inter

            # Actualiza el estado del paciente a "Internado"
            paciente.estado_pac = '1'  # Suponiendo que '1' es el código para "Internado"
            paciente.save()

            internacion.save()

            return redirect('internaciones')

    else:
        formulario = forminternacion(pacientes_disponibles=pacientes_disponibles)

    return render(request, 'agregarinternacion.html', {'formulario': formulario})

def asignar_obra_coseguro(request, paciente_id):
    paciente = Pacientes.objects.get(id=paciente_id)

    if request.method == 'POST':
        form = AsignarObraCoseguroForm(request.POST)
        if form.is_valid():
            obra_coseguro = form.save(commit=False)
            obra_coseguro.paciente = paciente
            obra_coseguro.save()
            return redirect('listapacientes')
    else:
        form = AsignarObraCoseguroForm()

    return render(request, 'obra.html', {'form': form, 'paciente': paciente})

def mostrarObras(request):
    obras = Obras_Pacientes.objects.all()

    context={
        'obras': obras
    }

    return render(request, 'mostrarobra.html', context)

def altaPaciente(request, internaciones_id):
    internacion = Internaciones.objects.get(id=internaciones_id)

    if request.method=='POST':
        form = forminternacion(request.POST, instance = internacion)
        internacion = form.save(commit=False)
            # Establecer la fecha y hora de egreso al momento del formulario
        internacion.fecha_egreso = form.cleaned_data['fecha_egreso']
        internacion.hora_egreso = form.cleaned_data['hora_egreso']

        paciente = internacion.paciente_inter
        paciente.estado_pac = '2'
        if not internacion.fecha_egreso:
            internacion.fecha_egreso = datetime.date.today()
        if not internacion.hora_egreso:
            internacion.hora_egreso = datetime.datetime.now().time()
        paciente.save()

        internacion.save()

        return redirect('internaciones')
    else:
        form = forminternacion(instance=internacion)

    context={
        'form': form,
        'internacion': internacion
    }

    return render(request, 'alta.html',context)

def verpac_per(request):
    lista = Personal_Paciente.objects.all()

    context = {
        'lista': lista
    }

    return render(request, 'personal_paciente.html', context)

@login_required
def cargar_prescripcion(request, personal_paciente_id):
    if request.method == 'POST':
        form = formprescripcion(request.POST)
        if form.is_valid():
            prescripcion = form.save(commit=False)
            prescripcion.personal_paciente_id = personal_paciente_id
            prescripcion.save()
            return redirect('prescripciones', personal_paciente_id=personal_paciente_id)
    else:
        form = formprescripcion()

    return render(request, 'cargar_prescripcion.html', {'form': form})

@login_required
def ver_prescripciones(request, personal_paciente_id):
    prescripciones = Prescripciones.objects.filter(personal_paciente_id=personal_paciente_id)
    return render(request, 'prescripcion.html', {'prescripciones': prescripciones})
