from django.db import models
from datetime import datetime,date
from .choices import *
from django.core.validators import *
from django.contrib.auth.models import *
from django.utils import timezone

#----------------------------------------------- Categoría -----------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=150,validators=[MinLengthValidator(3)],verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=200,validators=[MinLengthValidator(5)],verbose_name='Descripcion',blank=True,null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']

#----------------------------------------------- Tipo de Producto -----------------------------------------------
class Tipo(models.Model):
    nombre = models.CharField(max_length=150,validators=[MinLengthValidator(3)],verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=300,validators=[MinLengthValidator(3)],verbose_name='Descripción',blank=True,null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['id']

#----------------------------------------------- Ubicación -----------------------------------------------
class Ubicacion(models.Model):
    departamento = models.CharField(max_length=50,validators=[MinLengthValidator(1)],choices=Departamentos,default='1',verbose_name='Departamento')
    ciudad = models.CharField(max_length=50,validators=[MinLengthValidator(1)],choices=Ciudades,default='1',verbose_name='Ciudad')
    
    def __str__(self):
        return f"{self.get_departamento_display()} - {self.get_ciudad_display()}"
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'Ubicacion'
        ordering = ['id']


#----------------------------------------------- Producto -----------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=150,validators=[MinLengthValidator(3)],verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=150,validators=[MinLengthValidator(3)],verbose_name='Descripcion',blank=True,null=True)
    stock = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(10000)],verbose_name='Stock')
    precio = models.DecimalField(default=0.00,max_digits=9,decimal_places=2,validators=[MinValueValidator(0.00)])
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    tipo_pro = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']
        
#----------------------------------------------- Persona -----------------------------------------------
class Persona(models.Model):
    rol = models.CharField(max_length=1,choices=Roles,default='1',verbose_name='Rol de usuario')
    nombres = models.CharField(max_length=30,validators=[MinLengthValidator(3)],verbose_name='Nombres')
    apellidos = models.CharField(max_length=30,validators=[MinLengthValidator(3)],verbose_name='Apellidos')
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    correo = models.EmailField(max_length=100,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.CharField(max_length=15,verbose_name='Teléfono')
    numero_documento = models.CharField(max_length=20,unique=True,verbose_name='Número de Documento')
    usuario = models.CharField(max_length=150,unique=True,verbose_name='Usuario')
    password = models.CharField(max_length=128,verbose_name='Contraseña')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'Persona'
        ordering = ['id']
        
#----------------------------------------------- Cliente -----------------------------------------------
class Cliente(models.Model):
    tipo_persona = models.CharField(max_length=2,choices=Tipo_Persona_Choices,default='PN',verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=100,validators=[MinLengthValidator(3)],verbose_name='Nombres',null=True, blank=True)
    apellidos = models.CharField(max_length=100,validators=[MinLengthValidator(3)],verbose_name='Apellidos',null=True,blank=True)
    razon_social = models.CharField(max_length=150,verbose_name='Razon Social',null=True,blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex='^\d+$', message='El número de documento debe contener solo dígitos.')],verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=254,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.DecimalField(default=0,max_digits=10,decimal_places=0,validators=[MinValueValidator(0000000000)])
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150,validators=[MinLengthValidator(3)],null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.razon_social} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'
        db_table = 'Cliente'
        ordering = ['id']

#----------------------------------------------- Venta -----------------------------------------------

class Venta(models.Model):
    num_factura = models.CharField(max_length=20, primary_key=True, editable=False)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')

    def __str__(self):
        return self.num_factura

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'


#----------------------------------------------- Proveedor -----------------------------------------------

class Proveedor(models.Model):
    tipo_persona = models.CharField(max_length=2,choices=Tipo_Persona_Choices, default='PN',verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=100,validators=[MinLengthValidator(3)],verbose_name='Nombres',null=True, blank=True)
    apellidos = models.CharField(max_length=100,validators=[MinLengthValidator(3)],verbose_name='Apellidos',null=True,blank=True)
    razon_social = models.CharField(max_length=150,verbose_name='Razon Social',null=True,blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex='^\d+$', message='El número de documento debe contener solo dígitos.')],verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=254,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.DecimalField(default=0,max_digits=10,decimal_places=0,validators=[MinValueValidator(0000000000)])
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150,validators=[MinLengthValidator(3)],null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.razon_social} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'
        
#----------------------------------------------- Normativas -----------------------------------------------
class Normativa(models.Model):
    decreto=models.CharField(max_length=20,validators=[MinLengthValidator(3)],verbose_name='Decreto')
    descripcion=models.CharField(max_length=500,validators=[MinLengthValidator(10)],verbose_name='Descripción')
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.decreto
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        db_table = 'Normativa'
        
#----------------------------------------------- Compras -----------------------------------------------

class Compra(models.Model):
    cantidad = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)],verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=9,decimal_places=2,validators=[MinValueValidator(0.00)],verbose_name='Precio Unitario')
    precio_total = models.DecimalField(max_digits=9,decimal_places=2,validators=[MinValueValidator(0.00)],verbose_name='Precio Total',editable=False)
    fecha_ingreso = models.DateField(default=datetime.now,verbose_name='Fecha de Ingreso')
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Compra de {self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compra'
        ordering = ['id']

#----------------------------------------------- Detalles de Compras -----------------------------------------------

class DetalleCompra(models.Model):
    cantidad = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)],verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=9,decimal_places=2,validators=[MinValueValidator(0.00)],verbose_name='Precio Unitario')
    precio_total = models.DecimalField(max_digits=9,decimal_places=2,validators=[MinValueValidator(0.00)],verbose_name='Precio Total',editable=False)
    fecha_ingreso = models.DateField(default=datetime.now,verbose_name='Fecha de Ingreso')
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Detalle de Compra: {self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compras'
        db_table = 'DetalleCompra'
        ordering = ['id']