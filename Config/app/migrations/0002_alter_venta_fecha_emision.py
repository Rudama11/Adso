# Generated by Django 5.1.1 on 2024-09-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_emision',
            field=models.DateTimeField(verbose_name='Fecha de emision'),
        ),
    ]
