# Generated by Django 5.1.2 on 2024-10-16 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_venta_estado_venta_total_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total_venta',
        ),
    ]
