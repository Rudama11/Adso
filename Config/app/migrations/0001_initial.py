# Generated by Django 5.1 on 2024-08-23 20:22

import app.models
import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[app.models.validate_nombre], verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('1', 'Admin'), ('2', 'Usuario')], default='1', max_length=1, verbose_name='Rol de usuario')),
                ('nombres', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Apellidos')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('correo', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator()], verbose_name='Correo')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('numero_documento', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de documento debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de Documento')),
                ('usuario', models.CharField(max_length=150, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Persona')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombres')),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True, verbose_name='Razon Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de documento debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='Correo')),
                ('telefono', models.DecimalField(decimal_places=0, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[app.models.validate_nombre], verbose_name='Municipio')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='app.departamentos')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'db_table': 'municipios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio Unitario')),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio Total')),
                ('fecha_ingreso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Ingreso')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'Compra',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Descripcion')),
                ('stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='Stock')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
                ('tipo_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decreto', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Decreto')),
                ('descripcion', models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Descripción')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Normativa',
                'verbose_name_plural': 'Normativas',
                'db_table': 'Normativa',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio Unitario')),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio Total')),
                ('fecha_ingreso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Ingreso')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalles de Compras',
                'db_table': 'DetalleCompra',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedor'),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicaciones', to='app.departamentos', verbose_name='Departamento')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ubicaciones', to='app.municipios', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Ubicación',
                'verbose_name_plural': 'Ubicaciones',
                'db_table': 'ubicacion',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='proveedor',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Persona')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombres')),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True, verbose_name='Razon Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de documento debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='Correo')),
                ('telefono', models.DecimalField(decimal_places=0, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Dirección')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Cliente',
                'db_table': 'Cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('num_factura', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('impuestos', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
            },
        ),
    ]
