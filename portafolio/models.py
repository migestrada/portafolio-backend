from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model


class RolUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    rol_usuario = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Empresa(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Funcion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    porcentaje_realizacion = models.IntegerField()
    creador = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    unidad = models.ForeignKey('Unidad', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TareaAsignada(models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    terminada = models.BooleanField(default=False)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)
    asigando = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_termino 


class Post(models.Model):
    author = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title