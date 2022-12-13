from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    relacion = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    #nacimiento = models.DateField(auto_now_add=False,auto_now=False)

class Familiar_nacimiento(models.Model):
    nombre=models.CharField(max_length=20)
    relacion = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    nacimiento = models.DateField()