from django.db import models

class familiar(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    relacion = models.CharField(max_length=64)
    nacimiento = models.DateField()
    telefono = models.IntegerField()

