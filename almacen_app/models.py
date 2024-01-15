from django.db import models
from django.contrib.auth.models import User

class CategoriaProveedor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    categoria = models.ForeignKey(CategoriaProveedor, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='proveedor')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return self.nombre
