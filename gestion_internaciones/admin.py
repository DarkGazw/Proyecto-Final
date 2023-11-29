from django.contrib import admin
from gestion_internaciones.models import Pacientes, Drogueria, Personal, Cargos, Obras_Sociales, Coseguros, Habitaciones, Internaciones, Obras_Pacientes, Personal_Paciente, Prescripciones

class agregarpacientes(admin.ModelAdmin):
    pass 

class agregardrogas(admin.ModelAdmin):
    pass

class agregarcargo(admin.ModelAdmin):
    pass

class agregarpersonal(admin.ModelAdmin):
    pass

class agregarobrasocial(admin.ModelAdmin):
    pass

class agregarcoseguros(admin.ModelAdmin):
    pass
class agregarhabitacion(admin.ModelAdmin):
    pass

class agregarinternaciones(admin.ModelAdmin):
    pass

class agragarhabitacion(admin.ModelAdmin):
    pass

class agregarinternacion(admin.ModelAdmin):
    pass

class agragarhabitacion(admin.ModelAdmin):
    pass

class agregarinternacion(admin.ModelAdmin):
    pass

class obras(admin.ModelAdmin):
    pass

class asignarpaciente(admin.ModelAdmin):
    pass
class prescripcion(admin.ModelAdmin):
    pass

admin.site.register(Pacientes)
admin.site.register(Drogueria)
admin.site.register(Cargos)
admin.site.register(Personal)
admin.site.register(Obras_Sociales)
admin.site.register(Coseguros)
admin.site.register(Habitaciones)
admin.site.register(Internaciones)
admin.site.register(Obras_Pacientes)
admin.site.register(Personal_Paciente)
admin.site.register(Prescripciones)