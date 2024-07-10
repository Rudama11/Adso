# Generated by Django 5.0.7 on 2024-07-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_cliente_cedula_remove_cliente_fecha_n_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='nit',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='NIT'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='razon_social',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Razón Social'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_persona',
            field=models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Persona'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombres',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres'),
        ),
    ]
