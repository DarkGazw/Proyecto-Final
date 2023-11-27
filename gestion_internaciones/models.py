from django.db import models

# Create your models here.


class Pacientes(models.Model):
    nombre_pac = models.CharField(max_length=30)
    apellido_pac = models.CharField(max_length=15)
    dni_pac = models.CharField(max_length=10)
    domicilio_pac = models.CharField(max_length=50)
    telefono_pac = models.CharField(max_length=12)
    estados_choices = [('1','Internado'),
    ('2', 'Alta'),
    ('3', 'Fallecido'),
    ('4', 'Espera')]
    estado_pac = models.CharField(
        max_length=10,
        choices=estados_choices, default='4'
    )
    def __str__(self):
        return self.nombre_pac

    
class Habitaciones(models.Model):
    ubicacion_hab = models.CharField(max_length=50)
    camas_hab = models.IntegerField()
    camasdispo_hab = models.IntegerField()

class Internaciones(models.Model):
    paciente_inter = models.ForeignKey("Pacientes", on_delete=models.CASCADE)
    habitacion_inter = models.ForeignKey("Habitaciones", on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)
    hora_ingreso = models.TimeField(auto_now_add=True)
    fecha_egreso = models.DateField(null=True, blank=True)
    hora_egreso = models.TimeField(null=True, blank=True)

class Cargos(models.Model):
    nombre_car = models.CharField(max_length=50)

class Personal(models.Model):
    nombre_per = models.CharField(max_length=30)
    apellido_per = models.CharField(max_length=15)
    dni_per = models.CharField(max_length=10)
    domicilio_per = models.CharField(max_length=50)
    telefono_per = models.CharField(max_length=12)
    cargo = models.ForeignKey("Cargos",on_delete=models.CASCADE)

class Obras_Sociales(models.Model):
    nombre_obra = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    prestaciones = models.TextField()

    def __str__(self):
        return self.nombre_obra

class Coseguros(models.Model):
    nombre_cos = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    prestaciones = models.TextField()

    def __str__(self):
        return self.nombre_cos
class Obras_Pacientes(models.Model):
    paciente = models.ForeignKey("Pacientes",on_delete=models.CASCADE)
    obra_social = models.ForeignKey("Obras_Sociales",on_delete=models.CASCADE)
    coseguro = models.ForeignKey("Coseguros",on_delete=models.CASCADE)

class Personal_Paciente(models.Model):
    personal_a_cargo = models.ForeignKey("Personal",on_delete=models.CASCADE)
    paciente = models.ForeignKey("Pacientes",on_delete=models.CASCADE)

class Drogueria(models.Model):
    nombre_drog = models.CharField(max_length=20)
    stock_drog = models.IntegerField()

class Prescripciones(models.Model):
    personal_paciente = models.ForeignKey("Personal_Paciente", on_delete=models.CASCADE)
    medicamentos = models.ForeignKey("Drogueria", on_delete=models.CASCADE)
    detalles_de_control = models.TextField()
