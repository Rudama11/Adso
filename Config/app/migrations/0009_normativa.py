# Generated by Django 5.0.6 on 2024-07-09 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_producto_tipo_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decreto', models.CharField(max_length=150, verbose_name='Decreto')),
                ('detalles', models.CharField(max_length=500, verbose_name='Detalles')),
                ('producto', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Normativa',
                'verbose_name_plural': 'Normativas',
                'db_table': 'Normativa',
            },
        ),
    ]
