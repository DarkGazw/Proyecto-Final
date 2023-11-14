from django.contrib import admin
from gestion_internaciones.models import Pacientes, Drogueria, Personal, Cargos, Obras_Sociales, Coseguros
# Register your models here.
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

admin.site.register(Pacientes)
admin.site.register(Drogueria)
admin.site.register(Cargos)
admin.site.register(Personal)
admin.site.register(Obras_Sociales)
admin.site.register(Coseguros)