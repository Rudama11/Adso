# Generated by Django 5.0.7 on 2024-07-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_ubicacion_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Usuario')], default='1', max_length=1, verbose_name='Rol de usuario'),
        ),
    ]