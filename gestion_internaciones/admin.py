from django.contrib import admin
from gestion_internaciones.models import Pacientes, Drogueria, Personal, Cargos, Obras_Sociales, Coseguros, Habitaciones, Internaciones

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

admin.site.register(Pacientes)
admin.site.register(Drogueria)
admin.site.register(Cargos)
admin.site.register(Personal)
admin.site.register(Obras_Sociales)
admin.site.register(Coseguros)
admin.site.register(Habitaciones)
admin.site.register(Internaciones)