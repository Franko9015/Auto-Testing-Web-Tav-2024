from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Proveedor, Cliente
from .forms import ProveedorForm, ClienteForm
from .forms import RegistroForm, CustomLoginForm

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'almacen_app/lista_proveedores.html', {'proveedores': proveedores})

def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()

    return render(request, 'almacen_app/registrar_proveedor.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'almacen_app/lista_clientes.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'almacen_app/registrar_cliente.html', {'form': form})

def index(request):
    return render(request, 'almacen_app/index.html')
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'almacen_app/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = CustomLoginForm()

    return render(request, 'almacen_app/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')