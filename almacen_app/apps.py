from django.apps import AppConfig
from django.contrib import admin

class AlmacenAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'almacen_app'

    def ready(self):
        # Importa tus modelos aquí para asegurarte de que Django esté completamente cargado
        from .models import Proveedor, Cliente
        admin.site.register(Proveedor)
        admin.site.register(Cliente)
