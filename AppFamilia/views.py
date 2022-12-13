from django.shortcuts import render
from .models import Familiar , Familiar_nacimiento
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
# Create your views here.

def familia(request):

    fran = Familiar(nombre = "Francisco", relacion = "Hermano", genero = "Masculino" , edad = 24)
    mama = Familiar(nombre = "Silvia", relacion = "Mama", genero = "Femenino" , edad = 65)
    gasty = Familiar(nombre = "Gasty", relacion = "Perro", genero = "Masculino" , edad = 14)
    fran.save()
    mama.save()
    gasty.save()
    str = f"Nombre: {fran.nombre}   Relacion:{fran.relacion}    Genero:{fran.genero}    Edad:{fran.edad}\nNombre: {mama.nombre}   Relacion:{mama.relacion}    Genero:{mama.genero}    Edad:{mama.edad}\nNombre: {gasty.nombre}   Relacion:{gasty.relacion}    Genero:{gasty.genero}    Edad:{gasty.edad}\n"
    return HttpResponse(str)

def famtemplate (request):
    fran = Familiar_nacimiento (nombre = "Francisco", relacion = "Hermano", genero = "Masculino" , edad = 24, nacimiento = datetime(1998,3,10))
    mama = Familiar_nacimiento (nombre = "Silvia", relacion = "Mama", genero = "Femenino" , edad = 65, nacimiento = datetime(1957,5,14))
    gasty = Familiar_nacimiento (nombre = "Gasty", relacion = "Perro", genero = "Masculino" , edad = 14, nacimiento =  datetime(2008,8,8))
    fran.save()
    mama.save()
    gasty.save()
    diccionario = {"fam1": fran, "fam2": mama, "fam3": gasty}
    plantilla = loader.get_template('templatefam.html')
    doc = plantilla.render(diccionario)
    return HttpResponse(doc)
    #return render(request,"AppFamilia/templatefam.html", {"fam1":fran, "fam2":mama, "fam3":gasty})
