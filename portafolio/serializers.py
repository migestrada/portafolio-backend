from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username', 'password', 'rut','nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['url', 'nombre', 'descripcion']

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['url', 'nombre', 'descripcion', 'empresa']

class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = ['url', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'porcentaje_realizacion', 'creador', 'unidad']

class TareaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaAsignada
        fields = ['url', 'fecha_inicio', 'fecha_termino', 'terminada', 'tarea', 'asigando', 'funcion']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text','created_date','published_date']