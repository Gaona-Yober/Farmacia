# views.py de tu aplicación
from django.shortcuts import render
from .models import Cliente, Venta, EmpleadoSucursal

def home(request):
    return render(request, 'inicio.html')

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'listar_ventas.html', {'ventas': ventas})

def empleados(request):
    empleados = EmpleadoSucursal.objects.all()
    return render(request, 'empleados_sucursales.html', {'empleados': empleados})