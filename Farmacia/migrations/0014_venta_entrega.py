# Generated by Django 5.1.5 on 2025-01-26 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmacia', '0013_remove_venta_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Farmacia.sucursal'),
        ),
    ]
