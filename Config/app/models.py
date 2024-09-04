from django.db import models
from datetime import datetime,date
from .choices import Roles,Tipo_Documento_Choices,Tipo_Persona_Choices
from django.core.validators import *
from django.contrib.auth.models import *
from django.core.exceptions import ValidationError
from django.utils.text import slugify

import re

def validate_nombre(value):
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
        raise ValidationError('El nombre solo puede contener letras y espacios.')

# ----------------------------------------------- Departamentos -----------------------------------------------
class Departamentos(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Departamento',null=False,blank=False,validators=[validate_nombre])

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = "Departamentos"
        db_table = 'departamentos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

# ----------------------------------------------- Municipios -----------------------------------------------
class Municipios(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Municipio',null=False,blank=False,validators=[validate_nombre])
    departamento = models.ForeignKey(Departamentos,on_delete=models.CASCADE,related_name='municipios')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = "Municipios"
        db_table = 'municipios'
        ordering = ['id']

    def __str__(self):
        return self.nombre

#----------------------------------------------- Categoría -----------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=200,validators=[MinLengthValidator(5),validate_nombre],verbose_name='Descripcion',blank=True,null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']

#----------------------------------------------- Tipo de Producto -----------------------------------------------
class Tipo(models.Model):
    nombre = models.CharField(max_length=50,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=200,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Descripción',blank=True,null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['id']

# ----------------------------------------------- Ubicación -----------------------------------------------
class Ubicacion(models.Model):
    departamento = models.ForeignKey(Departamentos,on_delete=models.CASCADE,verbose_name='Departamento',related_name='ubicaciones')
    municipio = models.ForeignKey(Municipios,on_delete=models.CASCADE,verbose_name='Municipio',null=True,blank=True,related_name='ubicaciones')

    def __str__(self):
        return f"{self.departamento} - {self.municipio}"

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'ubicacion'
        ordering = ['id']
        
#----------------------------------------------- Persona -----------------------------------------------
class Persona(models.Model):
    rol = models.CharField(max_length=1,choices=Roles,default='1',verbose_name='Rol de usuario')
    nombres = models.CharField(max_length=100,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Nombres')
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de documento debe contener solo dígitos.')],verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=50,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de celular debe contener solo dígitos.')],verbose_name='Número de celular',null=True,blank=True)
    usuario = models.CharField(max_length=20,unique=True,verbose_name='Usuario')
    password = models.CharField(max_length=20,verbose_name='Contraseña')

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
    nombres = models.CharField(max_length=100,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Nombres',null=True, blank=True)
    razon_social = models.CharField(max_length=150,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Razon Social',null=True,blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de documento debe contener solo dígitos.')],verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=50,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de celular debe contener solo dígitos.')],verbose_name='Número de celular',null=True,blank=True)
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50,validators=[MinLengthValidator(3)],null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.razon_social} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'
        db_table = 'Cliente'
        ordering = ['id']

#----------------------------------------------- Proveedor -----------------------------------------------

class Proveedor(models.Model):
    tipo_persona = models.CharField(max_length=2,choices=Tipo_Persona_Choices, default='PN',verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=100,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Nombres',null=True, blank=True)
    razon_social = models.CharField(max_length=150,validators=[MinLengthValidator(3),validate_nombre],verbose_name='Razon Social',null=True,blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de documento debe contener solo dígitos.')],verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=50,validators=[EmailValidator()],verbose_name='Correo')
    telefono = models.CharField(max_length=10,validators=[MinLengthValidator(8),RegexValidator(regex=r'^\d+$', message='El número de celular debe contener solo dígitos.')],verbose_name='Número de celular',null=True,blank=True)
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50,validators=[MinLengthValidator(3)],null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.razon_social} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'
                
#----------------------------------------------- Compras -----------------------------------------------

class Compras(models.Model):
    num_factura = models.CharField(max_length=20, verbose_name='Número de Factura')
    fecha_compra = models.DateTimeField(verbose_name='Fecha de Compra')
    nombre_producto = models.CharField(max_length=50, validators=[MinLengthValidator(3)], verbose_name='Nombre')
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)], verbose_name='Cantidades')
    precio = models.DecimalField(default=0.0, max_digits=9, decimal_places=1)
    impuestos = models.DecimalField(default=0.0, max_digits=9, decimal_places=1)
    total = models.DecimalField(default=0.0, max_digits=9, decimal_places=1)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura {self.num_factura} - Proveedor: {self.proveedor.nombre}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compras'
        ordering = ['id']

#----------------------------------------------- Producto -----------------------------------------------
class Producto(models.Model):
    producto = models.ForeignKey(Compras, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150, validators=[MinLengthValidator(3)], verbose_name='Descripción', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo_pro = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']

#----------------------------------------------- Venta -----------------------------------------------
class Venta(models.Model):
    num_factura = models.CharField(max_length=10, primary_key=True, editable=False)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura {self.num_factura} - Cliente: {self.cliente.nombre}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'

#----------------------------------------------- Normativas -----------------------------------------------
class Normativa(models.Model):
    decreto=models.CharField(max_length=25,validators=[MinLengthValidator(3)],verbose_name='Decreto')
    descripcion=models.CharField(max_length=200,validators=[MinLengthValidator(10),validate_nombre],verbose_name='Descripción')
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.decreto
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        db_table = 'Normativa'