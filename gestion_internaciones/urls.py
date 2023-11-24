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
    path('agregarinternacion/', views.agregarinternacion, name='agregarinternacion'),
]