# Generated by Django 5.1.1 on 2024-09-11 21:19

import app.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_campos], verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(5), app.models.validate_nombre], verbose_name='Descripcion')),
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
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Usuarios')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_nombre], verbose_name='Nombres')),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_nombre], verbose_name='Razon Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de documento debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de celular debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de celular')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Dirección')),
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
                ('nombre', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_campos], verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_nombre], verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('nombres', models.CharField(blank=True, max_length=30, validators=[app.models.validate_nombre])),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
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
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_campos], verbose_name='Nombre')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
                ('tipo_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo', verbose_name='Tipo de producto')),
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
                ('decreto', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_campos], verbose_name='Decreto')),
                ('descripcion', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10), app.models.validate_nombre], verbose_name='Descripción')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Normativa',
                'verbose_name_plural': 'Normativas',
                'db_table': 'Normativa',
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_factura', models.CharField(max_length=20, verbose_name='Número de Factura')),
                ('fecha_compra', models.DateTimeField(verbose_name='Fecha de Compra')),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad')),
                ('precio', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio $(Cop)')),
                ('iva', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='IVA (%)')),
                ('total', models.IntegerField(default=0, verbose_name='Total $(Cop)')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='app.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedor')),
            ],
            options={
                'verbose_name': 'Compras',
                'verbose_name_plural': 'Compras',
                'db_table': 'Compras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad en Stock')),
                ('precio', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio(Cop)')),
                ('nombre_pro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'db_table': 'Stock',
                'ordering': ['id'],
            },
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
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Usuarios')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_nombre], verbose_name='Nombres')),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(3), app.models.validate_nombre], verbose_name='Razon Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de documento debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='El número de celular debe contener solo dígitos.', regex='^\\d+$')], verbose_name='Número de celular')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Dirección')),
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
                ('num_factura', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('impuestos', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
            },
        ),
    ]
