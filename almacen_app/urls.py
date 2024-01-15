from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
