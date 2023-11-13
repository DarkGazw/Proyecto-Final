from django.shortcuts import render
from gestion_internaciones.models import Pacientes
# Create your views here.
def listapacientes (request):
    pacientes = Pacientes.objects.all()
    
    context = {
        'pacientes': pacientes,
    }
    
    return render(request, 'pacientes.html', context) 