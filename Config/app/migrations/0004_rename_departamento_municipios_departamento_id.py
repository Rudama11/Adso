# Generated by Django 5.1 on 2024-08-26 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_departamento_id_municipios_departamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='municipios',
            old_name='departamento',
            new_name='departamento_id',
        ),
    ]
