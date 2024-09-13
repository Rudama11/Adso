# Generated by Django 5.1.1 on 2024-09-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_email_alter_customuser_nombres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(choices=[('superadmin', 'Superadministrador'), ('admin', 'Administrador'), ('usuario', 'Usuario normal')], default='usuario', max_length=10, verbose_name='Tipo de usuario'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Contraseña'),
        ),
    ]
