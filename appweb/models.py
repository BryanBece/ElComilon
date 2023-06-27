from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import Permission

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
list_tipo_plato = [
    (0, 'Entrada'),
    (1, 'Principal'),
    (2, 'Postre'),
    (3, 'Liquidos')

] 
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='producto', null=False)
    tipo_plato = models.IntegerField(choices=list_tipo_plato)


    def __str__(self):
        return self.nombre

