from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    clave = models.CharField(max_length=15)

