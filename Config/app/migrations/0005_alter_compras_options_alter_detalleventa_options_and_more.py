# Generated by Django 5.1.1 on 2024-09-13 18:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_venta_options_alter_customuser_password_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compras',
            options={'ordering': ['id'], 'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name': 'Detalle de Venta', 'verbose_name_plural': 'Detalles de Ventas'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.RemoveField(
            model_name='compras',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='iva',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='total',
        ),
        migrations.RemoveField(
            model_name='detallecompra',
            name='total',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='total',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='impuestos',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='IVA (%)'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio Unitario'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='iva',
            field=models.PositiveIntegerField(default=19, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio(Cop)'),
        ),
    ]
