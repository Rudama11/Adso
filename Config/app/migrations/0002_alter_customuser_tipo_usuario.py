# Generated by Django 5.1.2 on 2024-10-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(choices=[('superuser', 'Super Usuario'), ('admin', 'Administrador'), ('usuario', 'Usuario')], default='superuser', max_length=10, verbose_name='Tipo de usuario'),
        ),
    ]
