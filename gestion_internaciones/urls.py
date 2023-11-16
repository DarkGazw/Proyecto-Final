from django.contrib import admin
from django.urls import path
from gestion_internaciones import views

urlpatterns = [
    path('pacientes/', views.listapacientes, name='listapacientes'),
    path('agregarpaciente/', views.agregarpaciente, name='agregarpaciente'),
    path('drogueria/', views.listadrogueria, name= 'listadrogueria'),
    path('agregardroga/', views.agregardroga, name= 'agregardroga')
]