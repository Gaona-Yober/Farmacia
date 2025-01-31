from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100, default="(L)")
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    ci = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.nombre


class Transferencia(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    sucursal_origen = models.ForeignKey(
        Sucursal,
        related_name="transferencias_origen",
        on_delete=models.CASCADE
    )
    sucursal_destino = models.ForeignKey(
        Sucursal,
        related_name="transferencias_destino",
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField()
    fecha_transferencia = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.medicamento.sucursal != self.sucursal_origen:
            raise ValidationError(
                f"El medicamento '{self.medicamento.nombre}' no pertenece a la sucursal de origen '{self.sucursal_origen.nombre}'."
            )

        if self.medicamento.stock < self.cantidad:
            raise ValidationError(
                f"No hay suficiente stock de '{self.medicamento.nombre}' en la sucursal de origen. "
                f"Stock disponible: {self.medicamento.stock}, solicitado: {self.cantidad}."
            )

    def save(self, *args, **kwargs):
        self.clean()

        self.medicamento.stock -= self.cantidad
        self.medicamento.save()

        medicamento_destino, created = Medicamento.objects.get_or_create(
            nombre=self.medicamento.nombre,
            sucursal=self.sucursal_destino,
            defaults={
                'descripcion': self.medicamento.descripcion,
                'precio': self.medicamento.precio,
                'stock': 0,
            }
        )
        medicamento_destino.stock += self.cantidad
        medicamento_destino.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transferencia de {self.cantidad} {self.medicamento.nombre} de {self.sucursal_origen} a {self.sucursal_destino}"


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entrega = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    def actualizar_stock(self):
        if self.medicamento.stock >= self.cantidad:
            self.medicamento.stock -= self.cantidad
            self.medicamento.save()
        else:
            raise ValueError(
                f"Error: No hay suficiente stock de '{self.medicamento.nombre}' para completar la venta. "
                f"Stock disponible: {self.medicamento.stock}, cantidad solicitada: {self.cantidad}."
            )

    def save(self, *args, **kwargs):

        self.precio_unitario = self.medicamento.precio
        self.precio_final = self.precio_unitario * self.cantidad
        self.actualizar_stock()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.cantidad} {self.medicamento.nombre} a {self.cliente.nombre if self.cliente else 'Sin cliente'}"


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='farmacia_users',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='farmacia_users_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username

class EmpleadoSucursal(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.sucursal.nombre}"

