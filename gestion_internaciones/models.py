from django.db import models

# Create your models here.
class Pacientes(models.Model):
    nom_pac = models.CharField(max_length=50)
    ape_pac = models.CharField(max_length=50)
    dni_pac = models.CharField(max_length=50)
    estado_pac = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_pac