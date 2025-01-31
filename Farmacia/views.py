# views.py de tu aplicación
from django.shortcuts import render
from .models import Cliente, Venta, EmpleadoSucursal, Medicamento, Sucursal


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

def listar_medicamentos(request):
    sucursales = Sucursal.objects.all()
    sucursal_id = request.GET.get('sucursal', None)

    if sucursal_id:
        medicamentos = Medicamento.objects.filter(sucursal_id=sucursal_id)
    else:
        medicamentos = Medicamento.objects.all()

    return render(request, 'medicamentos.html', {
        'medicamentos': medicamentos,
        'sucursales': sucursales,
        'sucursal_id': int(sucursal_id) if sucursal_id else None
    })

def inicioClientes(request):
    return render(request, 'inicio_cliente.html')

def registroadministrador(request):
    return render(request, 'administrador_registro.html')

def registroempleados(request):
    return render(request, 'empleados_registro.html')

