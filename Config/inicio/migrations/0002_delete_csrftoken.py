# Generated by Django 5.0.7 on 2024-08-01 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CsrfToken',
        ),
    ]
