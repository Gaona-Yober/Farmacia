"""
URL configuration for DjangoProjectFarmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Farmacia import views
from Farmacia.views import vista_administrador

urlpatterns = [
    path('', views.home, name='inicio'),

    # Administrador
    path('admin/', admin.site.urls),

    path('cliente/', views.cliente, name='listar_clientes'),
    path('venta/', views.ventas, name='listar_venta'),
    path('empleadosucursal/', views.empleados, name='empleado_sucursales'),
    path('medicamento/', views.listar_medicamentos, name='listar_medicamentos'),
    path('iniciocliente/', views.inicioClientes, name='cliente'),
    path('registroadministrador/', views.registroadministrador, name='registroadministrador'),
    path('registroempleados/', views.registroempleados, name='registroempleados'),
    path('vistaadministrador/', vista_administrador, name='vista_administrador'),
]
