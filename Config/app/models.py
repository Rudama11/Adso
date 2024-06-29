from django.db import models
from datetime import datetime

opc_generos = [
    ('male', 'Male'),
    ('female', 'Female'),
]

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
#-----------------------------------------------------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categ = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_prod = models.ImageField(upload_to='product/%y/%m/%d', null=True, blank=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']
 
 #-----------------------------------------------------------------------------------------      
class Tipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    apellido= models.CharField(max_length=150, verbose_name='Apellido', unique=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['id']
        
#---------------------------------------------------------------------------------------------------------------
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
    #genero=models.CharField(max_length=50)
    # avatar=models.ImageField(upload_to='',null=True, blank=True)
    tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE)
    
    def str(self):
        return self.nombres
    
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table = 'Empleado'
        #ordering=[id]

#----------------------------------------------------------------------------------------------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    fecha_n = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=10, choices=opc_generos, default='male', verbose_name='Sexo')
    correo = models.EmailField(max_length=150, verbose_name='Correo')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']
#-------------------------------------------------------------------------------------------------------------
      
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

#-------------------------------------------------------------------------------------------------------------
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
