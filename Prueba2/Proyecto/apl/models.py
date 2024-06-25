from django.db import models
from datetime import datetime
from apl.choices import opc_generos


class Cliente(models.Model):
    Nombres = models.CharField(max_length=150, verbose_name='Nombres')
    Apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    Cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    Fecha_n = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    Direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion')
    Sexo = models.CharField(max_length=10, choices=opc_generos, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        # ordering = [id]

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        # ordering = [id]

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categ = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image_prod = models.ImageField(upload_to='product/%Y/%m/&d', null=True, blank=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        #ordering = [id]

class Venta(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        #ordering = [id]

class DetVenta(models.Model):
    fk_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name
    
    class Meta:
        verbose_name = 'DetVenta'
        verbose_name_plural = 'DetalleVentas'
        db_table = 'DetVenta'
        #ordering = [id]

class Tipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        db_table='Tipo'

class Empleado(models.Model):
    categ = models.ManyToManyField(Categoria)
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellido = models.CharField(max_length=150, verbose_name='Nombres', null=True, blank=True)
    cedula = models.CharField(max_length=11, unique=True, verbose_name='Cedula')
    fecha_registo = models.DateField(default= datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de registro')
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/d', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombres
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'
        #ordering = [id]