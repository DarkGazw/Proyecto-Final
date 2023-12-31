from django.contrib import admin
from django.urls import path
from gestion_internaciones import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.listapacientes, name='listapacientes'),
    path('agregarpaciente/', views.agregarpaciente, name='agregarpaciente'),
    path('personal/', views.listaPersonal, name='listapersonal'),
    path('agregardroga/', views.agregardroga, name= 'agregardroga'),
    path('listadrogueria/', views.listadroga, name='listadrogueria'),
    path('internaciones/', views.listainternaciones, name='internaciones'),
    path('agregarinternacion/', views.agregar_internacion, name='agregarinternacion'),
    path('obra/<int:paciente_id>/', views.asignar_obra_coseguro, name='asignarObra'),
    path('obras/', views.mostrarObras, name='obras'),
    path('alta/<int:internaciones_id>', views.altaPaciente, name='alta'),
    path('per_pac/',views.pacientes_por_personal, name='per_pac'),
    path('cargar_prescripcion/<int:personal_paciente_id>/', views.cargar_prescripcion, name='cargar_prescripcion'),
    path('prescripcion/<int:personal_paciente_id>/', views.ver_prescripciones, name='prescripciones'),
]   