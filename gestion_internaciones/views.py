from django.shortcuts import render, redirect
from gestion_internaciones.models import Pacientes, Personal, Drogueria, Internaciones, Obras_Sociales, Coseguros, Obras_Pacientes, Prescripciones, Personal_Paciente
from gestion_internaciones.forms import FormPaciente, formdroga, forminternacion, AsignarObraCoseguroForm,formprescripcion, formalta
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
import datetime
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test

def medicos(user):
    return user.groups.filter(name='Grupo Medico').exists()
medicos_required = user_passes_test(medicos)

@login_required
def listapacientes (request):
    pacientes = Pacientes.objects.all()
    
    context = {
        'pacientes': pacientes,
    }
    
    return render(request, 'pacientes/pacientes.html', context) 

@login_required
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
    return render(request, 'pacientes/agregarpaciente.html', context)

@login_required
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

@login_required
def home(request):
    context = {}

    return render(request, 'home/home.html', context)

def enfermeria(user):
    return user.groups.filter(name='Enfermeria').exists()
enfermeria_required = user_passes_test(enfermeria)

@enfermeria_required
def agregardroga(request):
    formulario = formdroga()
    if request.method== 'POST':
        formulario = formdroga(request.POST)
        if formulario.is_valid(): 
            formulario.save()
            formulario = formdroga()
            return redirect('listadrogueria')
                
    context={
        'formulario': formulario
    }
    return render(request, 'drogueria/agregardroga.html', context)

@login_required
def listadroga(request):
    drogueria = Drogueria.objects.all()

    context={
        'drogueria': drogueria
    }

    return render(request, 'drogueria/listadrogueria.html', context)

@login_required
def listainternaciones(request):
    internaciones = Internaciones.objects.all()

    context={
        'internaciones' : internaciones

    }
    return render(request, 'internaciones/internaciones.html', context)

@login_required
def agregar_internacion(request):
    pacientes_disponibles = Pacientes.objects.exclude(estado_pac='1')

    if request.method == 'POST':
        formulario = forminternacion(request.POST, pacientes_disponibles=pacientes_disponibles)
        if formulario.is_valid():
            internacion = formulario.save(commit=False)
            internacion.fecha_egreso = None
            internacion.hora_egreso = None
            paciente = internacion.paciente_inter
            paciente.estado_pac = '1'  
            paciente.save()

            internacion.save()

            return redirect('internaciones')

    else:
        formulario = forminternacion(pacientes_disponibles=pacientes_disponibles)
    
    context={
        'formulario': formulario
    }

    return render(request, 'internaciones/agregarinternacion.html', context)

@login_required
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

    context={
        'form': form,
        'paciente': paciente
    }

    return render(request, 'seguro/obra.html', context)

@login_required
def mostrarObras(request):
    obras = Obras_Pacientes.objects.all()

    context={
        'obras': obras
    }

    return render(request, 'seguro/mostrarobra.html', context)

@login_required
def altaPaciente(request, internaciones_id):
    internacion = Internaciones.objects.get(id=internaciones_id)

    if request.method=='POST':
        form = formalta(request.POST, instance = internacion)
        internacion = form.save(commit=False)
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
        form = formalta(instance=internacion)

    context={
        'form': form,
        'internacion': internacion
    }

    return render(request, 'internaciones/alta.html',context)

@medicos_required
def pacientes_por_personal(request):
    if request.user.personal:
        pacientes_asignados = Personal_Paciente.objects.filter(personal_a_cargo=request.user.personal)
        return render(request, 'personal_paciente.html', {'pacientes_asignados': pacientes_asignados})
    else:
        return render(request, '', {'mensaje': 'No eres un miembro del personal'})

@medicos_required
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

    context={
        'form': form
    }

    return render(request, 'cargar_prescripcion.html', context)

@medicos_required
def ver_prescripciones(request, personal_paciente_id):
    prescripciones = Prescripciones.objects.filter(personal_paciente_id=personal_paciente_id)

    context={
        'prescripciones': prescripciones
    }
    return render(request, 'prescripcion.html', context)

