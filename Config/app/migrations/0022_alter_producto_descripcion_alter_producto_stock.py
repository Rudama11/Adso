# Generated by Django 5.0.7 on 2024-07-25 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_producto_descripcion_alter_producto_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0, max_length=10, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Stock'),
        ),
    ]
