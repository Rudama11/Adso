# Generated by Django 5.0.6 on 2024-07-06 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_ubicacion_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubicacion',
            old_name='Ciudad',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='Departamento',
            new_name='departamento',
        ),
    ]