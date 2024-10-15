# Generated by Django 5.1.2 on 2024-10-10 07:19

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
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_factura', models.CharField(max_length=20, verbose_name='Número de Factura')),
                ('fecha_compra', models.DateField(verbose_name='Fecha de Compra')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'Compras',
                'ordering': ['num_factura'],
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Departamento')),
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
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Persona')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres / Razón Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número de celular')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descripción')),
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Nombre de usuario')),
                ('nombres', models.CharField(blank=True, max_length=50, verbose_name='Nombres y apellidos')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='SuperUsuario')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Administrador')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Última conexión')),
                ('tipo_usuario', models.CharField(choices=[('superuser', 'Super Usuario'), ('admin', 'Administrador'), ('usuario', 'Usuario')], default='superuser', max_length=10, verbose_name='Tipo de usuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuarios',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Municipio')),
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
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
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
                ('decreto', models.CharField(max_length=50, unique=True, verbose_name='Decreto')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Normativa',
                'verbose_name_plural': 'Normativas',
                'db_table': 'Normativa',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_factura', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio Unitario')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='IVA (%)')),
                ('total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Total')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='app.compras')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalles de Compra',
                'db_table': 'DetalleCompra',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='compras',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedor'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad en Stock')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio(Cop)')),
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
                ('tipo_persona', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], default='PN', max_length=2, verbose_name='Tipo de Persona')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres / Razón Social')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('NIT', 'Numero de identificación tributaria')], default='CC', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Número de Documento')),
                ('correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número de celular')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_factura', models.CharField(max_length=10, unique=True)),
                ('fecha_emision', models.DateField(verbose_name='Fecha de emisión')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('iva', models.PositiveIntegerField(default=19, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('num_factura', models.CharField(blank=True, max_length=20, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stock')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='app.venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalles de Ventas',
                'db_table': 'DetalleVenta',
            },
        ),
    ]