# Generated by Django 5.0.7 on 2024-07-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_proveedor_nit_proveedor_numero_documento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='normativa',
            old_name='detalles',
            new_name='descripcion',
        ),
    ]