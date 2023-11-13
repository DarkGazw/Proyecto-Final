from django.contrib import admin
from gestion_internaciones.models import Pacientes

# Register your models here.
class agregarpacientes(admin.ModelAdmin):
    pass 

admin.site.register(Pacientes)