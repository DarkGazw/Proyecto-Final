from django.contrib import admin
from django.urls import path
from gestion_internaciones import views

urlpatterns = [
    path('pacientes/', views.listapacientes, name='listapacientes')
]