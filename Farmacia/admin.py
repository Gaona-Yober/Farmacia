from django.contrib import admin
from .models import Sucursal, Medicamento, Cliente, Transferencia, Venta
from .models import Usuario, EmpleadoSucursal
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','sucursal', 'stock')
    list_filter = ('sucursal',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('medicamento','cliente', 'precio_unitario', 'precio_final', 'entrega')

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha_transferencia')
    #search_fields = ('medicamento__nombre', 'sucursal_origen__nombre', 'sucursal_destino__nombre')

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ("username", "email", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Información adicional", {"fields": ("telefono", "direccion")}),
    )
admin.site.register(Sucursal)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Cliente)
admin.site.register(Transferencia, TransferenciaAdmin)
admin.site.register(Venta, VentaAdmin)

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(EmpleadoSucursal)
