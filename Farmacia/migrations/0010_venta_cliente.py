# Generated by Django 5.1.5 on 2025-01-26 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmacia', '0009_remove_venta_iva'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Farmacia.cliente'),
        ),
    ]
