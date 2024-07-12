from django.db import models
from datetime import datetime

Tipo_Documento_Choices = [
    ('CC','Cédula de ciudadanía'),
    ('CE','Cédula de extranjería'),
    ('TI','Tarjeta de identidad'),
    ('PA','Pasaporte'),
    ('NIT','Numero de identificación tributaria')
]

Tipo_Persona_Choices = [
    ('PN', 'Persona Natural'),
    ('PJ', 'Persona Jurídica')
]

opc_generos = [
    ('male', 'Male'),
    ('female', 'Female'),
]

#------------- Categoría ---------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion',blank=True,null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']

#-------------  Tipo de Producto ---------------------------------------------------
class Tipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=300, verbose_name='Descripción', blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['id']

#------------- Ubicación ---------------------------------------------------
class Ubicacion(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    departamento = models.CharField(max_length=100, verbose_name='Departamento')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    
    def __str__(self):
        return self.ciudad
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'Ubicacion'

#------------- Producto ---------------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion',blank=True,null=True)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    categ = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name='Categoría')
    tipo_pro = models.ForeignKey('Tipo', on_delete=models.CASCADE, verbose_name='Tipo')
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']
        
#------------- Empleado ---------------------------------------------------
class Empleado (models.Model):
    categ=models.ManyToManyField(Categoria)#Relacion de muchos a muchos
    nombres= models.CharField(max_length=150,verbose_name='Nombres')
    apellido=models.CharField(max_length=150,verbose_name='Apellidos')
    cedula=models.CharField(max_length=11,unique=True, verbose_name='Cedula')
    fecha_registro=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    fecha_creacion=models.DateTimeField(auto_now=True,verbose_name='Fecha de creacion') 
    edad=models.PositiveIntegerField(default=0)
    salario=models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    estado=models.BooleanField(default=True)
    tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE)
    
    def str(self):
        return self.nombres
    
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table = 'Empleado'
        #ordering=[id]

#------------- Cliente ---------------------------------------------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    tipo_documento = models.CharField(max_length=3, choices=Tipo_Documento_Choices, default='CC', verbose_name='Tipo de Documento')
    edad = models.PositiveIntegerField(default=0)
    correo = models.EmailField(max_length=150, verbose_name='Correo')
    cod_postal = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, verbose_name='Código Postal', null=True, blank=True)
    direccion = models.CharField(max_length=150, verbose_name='Dirección')
    telefono = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_tipo_documento_display()}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']

#------------- Venta ---------------------------------------------------

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        ordering = ['id']

#------------- Detalle de venta ---------------------------------------------------
class DetalleVenta(models.Model):
    fk_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)  

    def __str__(self):
        return self.prod.nombre

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        db_table = 'Detalle de Venta'
        ordering = ['id']
        
        
#------------- Proveedor ---------------------------------------------------

class Proveedor(models.Model):
    tipo_persona = models.CharField(max_length=2, choices=Tipo_Persona_Choices, default='PN', verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=100, verbose_name='Nombres', null=True, blank=True)
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos', null=True, blank=True)
    razon_social = models.CharField(max_length=150, verbose_name='Razon Social', null=True, blank=True)
    tipo_documento = models.CharField(max_length=3, choices=Tipo_Documento_Choices, default='CC', verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=20, verbose_name='Numero de Documento', null=True, blank=True)
    correo = models.EmailField()
    telefono = models.IntegerField(default=0)
    cod_postal = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, verbose_name='Ubicacion')
    direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.razon_social} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'
        
#------------- Normativas-----------------------------
class Normativa(models.Model):
    decreto=models.CharField(max_length=150,verbose_name='Decreto')
    detalles=models.CharField(max_length=500,verbose_name='Detalles')
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,default=True)
    
    def __str__(self):
        return self.decreto
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        db_table = 'Normativa'
        #ordering = ['id']
