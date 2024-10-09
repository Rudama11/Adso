from django.db import models
from .choices import Tipo_Documento_Choices,Tipo_Persona_Choices
from django.core.validators import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# ----------------------------------------------- Usuarios -----------------------------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo Nombre de usuario debe estar configurado')
        if not email:
            raise ValueError('El campo Correo electrónico debe estar configurado')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('superuser', 'Superuser'),
        ('admin', 'Administrador'),
        ('usuario', 'Usuario normal'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True, verbose_name='Nombre de usuario')
    nombres = models.CharField(max_length=50, blank=True, verbose_name='Nombres y apellidos')
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    is_superuser = models.BooleanField(default=False, verbose_name='SuperUsuario')
    is_staff = models.BooleanField(default=False, verbose_name='Administrador')
    is_active = models.BooleanField(default=True, verbose_name='Estado')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Última conexión')
    tipo_usuario = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='superuser',
        verbose_name='Tipo de usuario'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.nombres or self.username

    def get_short_name(self):
        return self.username

# ----------------------------------------------- Departamentos -----------------------------------------------
class Departamentos(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Departamento',null=False,blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = "Departamentos"
        db_table = 'departamentos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

# ----------------------------------------------- Municipios -----------------------------------------------
class Municipios(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Municipio',null=False,blank=False)
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
    nombre = models.CharField(max_length=50,verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=150,verbose_name='Descripcion',blank=True,null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']

#----------------------------------------------- Tipo de Producto -----------------------------------------------
class Tipo(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre',unique=True)
    descripcion = models.CharField(max_length=150,verbose_name='Descripción',blank=True,null=True)
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

#----------------------------------------------- Cliente -----------------------------------------------
class Cliente(models.Model):
    tipo_persona = models.CharField(max_length=2,choices=Tipo_Persona_Choices,default='PN',verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=150,verbose_name='Nombres / Razón Social',null=True, blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=11,verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=50,verbose_name='Correo')
    telefono = models.CharField(max_length=10,verbose_name='Número de celular',null=True,blank=True)
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50,null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.nombres} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']

#----------------------------------------------- Proveedor -----------------------------------------------

class Proveedor(models.Model):
    tipo_persona = models.CharField(max_length=2,choices=Tipo_Persona_Choices,default='PN',verbose_name='Tipo de Persona')
    nombres = models.CharField(max_length=150,verbose_name='Nombres / Razón Social',null=True, blank=True)
    tipo_documento = models.CharField(max_length=3,choices=Tipo_Documento_Choices,default='CC',verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=11,verbose_name='Número de Documento',null=True,blank=True)
    correo = models.EmailField(max_length=50,verbose_name='Correo')
    telefono = models.CharField(max_length=10,verbose_name='Número de celular',null=True,blank=True)
    ciudad = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50,null=True,blank=True,verbose_name='Dirección')
    
    def __str__(self):
        return f"{self.nombres if self.tipo_persona == 'PN' else self.nombres} - {self.get_tipo_persona_display()}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'
        ordering = ['id']

#----------------------------------------------- Producto -----------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    tipo_pro = models.ForeignKey('Tipo', on_delete=models.CASCADE, verbose_name='Tipo de producto')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']

#----------------------------------------------- Compras -----------------------------------------------
class Compras(models.Model):
    num_factura = models.CharField(max_length=20, verbose_name='Número de Factura', primary_key=True)  # Clave primaria
    fecha_compra = models.DateField(verbose_name='Fecha de Compra')  # Cambiado a DateField
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Factura {self.num_factura}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compras'
        ordering = ['num_factura']

#----------------------------------------------- Detalle Compra -----------------------------------------------
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE, related_name='detalles', to_field='num_factura')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Precio Unitario')
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='IVA (%)')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False, verbose_name='Total')

    @property
    def Total(self):
        subtotal = self.precio_unitario * self.cantidad
        return subtotal + (subtotal * self.iva / 100)

    def save(self, *args, **kwargs):
        self.total = self.Total  # Asigna el total calculado al campo 'total'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Detalle de Compra {self.compra.num_factura} - Producto: {self.producto.nombre}'

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'
        db_table = 'DetalleCompra'
        ordering = ['id']
#----------------------------------------------- Stock -----------------------------------------------
class Stock(models.Model):
    nombre_pro = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Cantidad en Stock')
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Precio(Cop)')

    def __str__(self):
        return f'{self.nombre_pro.nombre} - Stock: {self.cantidad}'

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        db_table = 'Stock'
        ordering = ['id']
#----------------------------------------------- Ventas -----------------------------------------------       
class Venta(models.Model):
    num_factura = models.CharField(max_length=10, unique=True)  # Ahora es único
    fecha_emision = models.DateField(verbose_name='Fecha de emisión', editable=True)  # Cambiado a DateField
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura {self.num_factura} - Cliente: {self.cliente.nombre}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
#----------------------------------------------- Detalle Venta -----------------------------------------------
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('Stock', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    iva = models.PositiveIntegerField(default=19, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    num_factura = models.CharField(max_length=20, null=True, blank=True)  # Agregar este campo

    def __str__(self):
        return f'Detalle de la venta {self.venta.num_factura} - Producto: {self.producto.nombre_pro.nombre}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
        db_table = 'DetalleVenta'
#----------------------------------------------- Normativas -----------------------------------------------
class Normativa(models.Model):
    decreto=models.CharField(max_length=50,verbose_name='Decreto')
    descripcion=models.CharField(max_length=150,verbose_name='Descripción')
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.decreto
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        db_table = 'Normativa'
        ordering = ['id']