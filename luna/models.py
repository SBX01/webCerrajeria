from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    
class agendaServicio(models.Model):
    nombre=models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    tipoServicio= models.ForeignKey(Servicio,on_delete=models.CASCADE)
    


