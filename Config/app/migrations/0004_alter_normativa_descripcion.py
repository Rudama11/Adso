# Generated by Django 5.1.1 on 2024-09-18 20:03

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_compras_total_detallecompra_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normativa',
            name='descripcion',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1), app.models.validate_nombre], verbose_name='Descripción'),
        ),
    ]
