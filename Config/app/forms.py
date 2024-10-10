from dataclasses import fields
from django import forms
from django_select2.forms import Select2Widget
from app.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404
import re

#---------------------------------------------------------- Usuario ----------------------------------------------------------

# Formulario exclusivo para la creación de usuarios.
class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',  # Etiqueta en español
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese contraseña', 'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='Confirmar Contraseña',  # Etiqueta en español
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme la contraseña', 'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True  # Enfocar el campo username
        self.fields['tipo_usuario'].choices = CustomUser.USER_TYPE_CHOICES  # Establecer las opciones de tipo de usuario

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Validación de solo letras, números y guiones
        if not re.match(r'^[a-zA-Z0-9-]+$', username):
            raise forms.ValidationError('El nombre de usuario solo puede contener letras, números y guiones.')
        
        # Validación de unicidad
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Ya existe un usuario con este nombre de usuario.')
        
        return username
    
    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        # Validación de solo letras
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombres):
            raise forms.ValidationError('Los nombres solo pueden contener letras y espacios.')
        return nombres

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validación de unicidad
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Validación de longitud mínima de la contraseña
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        # Validación de coincidencia de contraseñas
        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return confirm_password

    class Meta:
        model = CustomUser
        fields = ['tipo_usuario', 'username', 'nombres', 'email', 'password', 'confirm_password']  # Tipo de usuario al inicio
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese nombre de usuario', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese nombres y apellidos', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese correo electrónico', 'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'})  # Campo de selección para tipo de usuario
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Establecer la contraseña de forma segura

        # Activar permisos según el tipo de usuario seleccionado
        if self.cleaned_data['tipo_usuario'] == 'superuser':
            user.is_superuser = True
            user.is_staff = True
        elif self.cleaned_data['tipo_usuario'] == 'admin':
            user.is_superuser = False
            user.is_staff = True
        elif self.cleaned_data['tipo_usuario'] == 'usuario':
            user.is_superuser = False
            user.is_staff = False
        
        if commit:
            user.save()  # Guarda el usuario después de establecer la contraseña encriptada
        return user
    

# Formulario exclusivo para editar los usuarios.
from django import forms
import re
from .models import CustomUser  # Asegúrate de que la importación del modelo es correcta

class UsuarioEditForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',  # Etiqueta en español
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese nueva contraseña (dejar vacío si no quiere cambiar)', 'class': 'form-control'}),
        required=False  # Hacer el campo opcional
    )
    confirm_password = forms.CharField(
        label='Confirmar Contraseña',  # Etiqueta en español
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme nueva contraseña (dejar vacío si no quiere cambiar)', 'class': 'form-control'}),
        required=False  # Hacer el campo opcional
    )
    is_active = forms.ChoiceField(
        choices=[(True, 'Habilitado'), (False, 'Inhabilitado')],
        label='Estado del Usuario',  # Etiqueta en español
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=True  # O el valor que desees como predeterminado
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True  # Enfocar el campo username
        self.fields['tipo_usuario'].choices = CustomUser.USER_TYPE_CHOICES  # Establecer las opciones de tipo de usuario

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Validación de solo letras, números y guiones
        if not re.match(r'^[a-zA-Z0-9-]+$', username):
            raise forms.ValidationError('El nombre de usuario solo puede contener letras, números y guiones.')
        
        # Validación de unicidad, excluyendo el usuario actual
        if CustomUser.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un usuario con este nombre de usuario.')
        
        return username
    
    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        # Validación de solo letras
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombres):
            raise forms.ValidationError('Los nombres solo pueden contener letras y espacios.')
        return nombres

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validación de unicidad, excluyendo el usuario actual
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Validación de longitud mínima de la contraseña si se proporciona
        if password and len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        # Validación de coincidencia de contraseñas si se proporciona
        if password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return confirm_password

    class Meta:
        model = CustomUser
        fields = ['tipo_usuario', 'username', 'nombres', 'email', 'password', 'confirm_password', 'is_active']  # Agregar el campo is_active aquí
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese nombre de usuario', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese nombres y apellidos', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese correo electrónico', 'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'})  # Campo de selección para tipo de usuario
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        # Solo establecer la contraseña si se proporciona una nueva
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Establecer la nueva contraseña

        # Activar permisos según el tipo de usuario seleccionado
        if self.cleaned_data['tipo_usuario'] == 'superuser':
            user.is_superuser = True
            user.is_staff = True
        elif self.cleaned_data['tipo_usuario'] == 'admin':
            user.is_superuser = False
            user.is_staff = True
        elif self.cleaned_data['tipo_usuario'] == 'usuario':
            user.is_superuser = False
            user.is_staff = False
        
        # Establecer el estado activo/inactivo
        user.is_active = self.cleaned_data['is_active'] == 'True'

        if commit:
            user.save()  # Guarda el usuario después de establecer la contraseña si se ha cambiado
        return user


#---------------------------------------------------------- Categoría ----------------------------------------------------------
class CategoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True  # Enfocar el campo nombre

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if not re.match(r'^[\w\s.-]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras, números, espacios, guiones y puntos.')
        
        # Validación de unicidad
        if Categoria.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe una categoría con este nombre.')
        
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if descripcion and not re.match(r'^[\w\s.-]*$', descripcion):
            raise forms.ValidationError('La descripción solo puede contener letras, números, espacios, guiones y puntos.')
        return descripcion

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre', 'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese descripción', 'class': 'form-control'}),
        }

#---------------------------------------------------------- Tipo ----------------------------------------------------------

class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True  # Enfocar el campo nombre

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if not re.match(r'^[\w\s.-]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras, números, espacios, guiones y puntos.')
        
        # Validación de unicidad
        if Tipo.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un tipo de producto con este nombre.')
        
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if descripcion and not re.match(r'^[\w\s.-]*$', descripcion):
            raise forms.ValidationError('La descripción solo puede contener letras, números, espacios, guiones y puntos.')
        return descripcion

    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre', 'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese descripción', 'class': 'form-control'}),
        }
        
#---------------------------------------------------------- Ubicación ----------------------------------------------------------
class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['departamento', 'municipio']
        widgets = {
            'departamento': Select2Widget(attrs={'class': 'select2', 'placeholder': 'Seleccione el departamento'}),
            'municipio': Select2Widget(attrs={'class': 'select2', 'placeholder': 'Seleccione el municipio'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        departamento = cleaned_data.get('departamento')
        municipio = cleaned_data.get('municipio')

        if not municipio:
            raise ValidationError('Debe seleccionar un municipio.')

        if Ubicacion.objects.filter(departamento=departamento, municipio=municipio).exists():
            raise ValidationError('Esta combinación de departamento y municipio ya existe.')

        return cleaned_data
            
#---------------------------------------------------------- Cliente ----------------------------------------------------------
class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True
        self.initial_data = {
            'nombres': self.instance.nombres,
            'numero_documento': self.instance.numero_documento,
            'correo': self.instance.correo,
            'telefono': self.instance.telefono,
            'direccion': self.instance.direccion,
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        if not re.match(r'^[\w\s.-]+$', nombres):
            raise forms.ValidationError('Los nombres solo pueden contener letras, números, espacios, guiones y puntos.')
        return nombres

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        tipo_documento = self.cleaned_data.get('tipo_documento')

        # Validaciones dependiendo del tipo de documento
        if tipo_documento == 'NIT':
            if not re.match(r'^\d{9}-\d$', numero_documento):
                raise forms.ValidationError('El NIT debe ser un número con 9 dígitos seguido de un guion y un dígito.')
        elif tipo_documento == 'PA':
            if not re.match(r'^[a-zA-Z0-9]{6,}$', numero_documento):
                raise forms.ValidationError('El pasaporte debe ser alfanumérico y tener al menos 6 caracteres.')
        else:
            if not re.match(r'^\d{7,10}$', numero_documento):
                raise forms.ValidationError('El número de documento debe tener entre 7 y 10 dígitos.')

        # Validación de unicidad
        if Cliente.objects.filter(numero_documento=numero_documento).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un cliente con este número de documento.')

        return numero_documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\d{6,10}$', telefono):
            raise forms.ValidationError('El teléfono debe ser solo números, entre 6 y 10 dígitos.')
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Cliente.objects.filter(correo=correo).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un cliente con esta dirección de correo electrónico.')
        return correo

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese nombres','class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'placeholder': 'Ingrese número de documento','class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese correo','class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de celular','class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese dirección','class': 'form-control'}),}

#-------------------------------------------------------- Proveedor ----------------------------------------------------------
class ProveedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True
        self.initial_data = {
            'nombres': self.instance.nombres,
            'numero_documento': self.instance.numero_documento,
            'correo': self.instance.correo,
            'telefono': self.instance.telefono,
            'direccion': self.instance.direccion,
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        if not re.match(r'^[\w\s.-]+$', nombres):
            raise forms.ValidationError('Los nombres solo pueden contener letras, números, espacios, guiones y puntos.')
        return nombres

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        tipo_documento = self.cleaned_data.get('tipo_documento')

        # Validaciones dependiendo del tipo de documento
        if tipo_documento == 'NIT':
            if not re.match(r'^\d{9}-\d$', numero_documento):
                raise forms.ValidationError('El NIT debe ser un número con 9 dígitos seguido de un guion y un dígito.')
        elif tipo_documento == 'PA':
            if not re.match(r'^[a-zA-Z0-9]{6,}$', numero_documento):
                raise forms.ValidationError('El pasaporte debe ser alfanumérico y tener al menos 6 caracteres.')
        else:
            if not re.match(r'^\d{7,10}$', numero_documento):
                raise forms.ValidationError('El número de documento debe tener entre 7 y 10 dígitos.')

        # Validación de unicidad
        if Proveedor.objects.filter(numero_documento=numero_documento).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un proveedor con este número de documento.')

        return numero_documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\d{6,10}$', telefono):
            raise forms.ValidationError('El teléfono debe ser solo números, entre 6 y 10 dígitos.')
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Proveedor.objects.filter(correo=correo).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un proveedor con esta dirección de correo electrónico.')
        return correo

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese nombres','class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'placeholder': 'Ingrese número de documento','class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese correo','class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de celular','class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese dirección','class': 'form-control'}),}

#--------------------------------------------------------- Producto ----------------------------------------------------------
class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True  # Enfocar el campo nombre

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if not re.match(r'^[\w\s.-]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras, números, espacios, guiones y puntos.')
        
        # Validación de unicidad
        if Producto.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un producto con este nombre.')
        
        return nombre

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('Debe seleccionar una categoría.')
        return categoria

    def clean_tipo_pro(self):
        tipo_pro = self.cleaned_data.get('tipo_pro')
        if not tipo_pro:
            raise forms.ValidationError('Debe seleccionar un tipo de producto.')
        return tipo_pro

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pro': forms.Select(attrs={'class': 'form-control'}),
        }

#------------------------------------------------------- Normativa----------------------------------------------------------
class NormativaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['decreto'].widget.attrs['autofocus'] = True  # Enfocar el campo decreto

    def clean_decreto(self):
        decreto = self.cleaned_data.get('decreto')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if not re.match(r'^[\w\s.-]+$', decreto):
            raise forms.ValidationError('El decreto solo puede contener letras, números, espacios, guiones y puntos.')

        # Validación de unicidad
        if Normativa.objects.filter(decreto=decreto).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe una normativa con este decreto.')
        
        return decreto

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        # Validación de solo alfanuméricos, espacios, guiones y puntos
        if descripcion and not re.match(r'^[\w\s.-]*$', descripcion):
            raise forms.ValidationError('La descripción solo puede contener letras, números, espacios, guiones y puntos.')
        return descripcion

    class Meta:
        model = Normativa
        fields = '__all__'
        widgets = {
            'decreto': forms.TextInput(attrs={'placeholder': 'Ingrese decreto', 'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese descripción', 'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),  # Suponiendo que 'producto' es un ForeignKey
        }

#---------------------------------------------------------- Ventas ----------------------------------------------------------

class VentaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['autofocus'] = True
        
        # Establecemos la fecha actual como valor inicial del campo fecha_emision
        if not self.instance.pk:
            self.fields['fecha_emision'].initial = timezone.now().strftime('%Y-%m-%d')

    def clean_num_factura(self):
        num_factura = self.cleaned_data.get('num_factura')
        # Validación de unicidad
        if Venta.objects.filter(num_factura=num_factura).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe una venta con este número de factura.')
        
        # Validación de solo caracteres alfanuméricos
        if not re.match(r'^[\w-]+$', num_factura):
            raise forms.ValidationError('El número de factura solo puede contener letras, números y guiones.')
        
        return num_factura

    def clean_fecha_emision(self):
        fecha_emision = self.cleaned_data.get('fecha_emision')
        # Validación de que la fecha no sea en el futuro
        if fecha_emision and fecha_emision > timezone.now().date():
            raise forms.ValidationError('La fecha de emisión no puede ser mayor a la actual. Solo se permiten fechas hasta hoy.')
        
        return fecha_emision

    class Meta:
        model = Venta
        fields = ['num_factura', 'fecha_emision', 'cliente']  # Especifica los campos a incluir
        widgets = {
            'num_factura': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un número de factura',
                    'class': 'form-control'
                }
            ),
            'fecha_emision': forms.DateInput(
                attrs={
                    'placeholder': 'Seleccione la fecha de emisión',
                    'class': 'form-control',
                    'type': 'date'  # Cambiado a 'date' para manejar solo fechas
                }
            ),
            'cliente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

#----------------------------------------------------- Dellate Ventas---------------------------------------------------------------
from django import forms
from .models import DetalleVenta, Producto  # Asegúrate de importar tus modelos

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad', 'iva', 'total', 'precio', 'num_factura']
        widgets = {
            'venta': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_venta'}),
            'producto': forms.Select(attrs={'class': 'form-control', 'id': 'id_producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'value': 0, 'id': 'id_cantidad'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_precio'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100, 'id': 'id_iva'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_total'}),
            'num_factura': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_num_factura'})
        }

    def clean_producto(self):
        producto = self.cleaned_data.get('producto')
        if not producto:
            raise forms.ValidationError('Este campo es obligatorio.')
        return producto

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None:
            raise forms.ValidationError('Este campo es obligatorio.')
        if cantidad < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa.')
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None:
            raise forms.ValidationError('Este campo es obligatorio.')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_iva(self):
        iva = self.cleaned_data.get('iva')
        if iva is None:
            raise forms.ValidationError('Este campo es obligatorio.')
        if iva < 0 or iva > 100:
            raise forms.ValidationError('El IVA debe estar entre 0 y 100.')
        return iva

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if producto:
            precio_unitario = producto.precio  # Obtén el precio desde el modelo Producto
            cleaned_data['precio'] = precio_unitario  # Almacenar el precio unitario

        if cantidad and 'precio' in cleaned_data:
            total = cantidad * cleaned_data['precio']  # Calcular total
            cleaned_data['total'] = total

        return cleaned_data

#---------------------------------------------------- Producto Filter Form ----------------------------------------------------------
class ProductoFilterForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'class': 'form-control'})
    )

    categoria = forms.ModelChoiceField(
        required=False,
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tipo_pro = forms.ModelChoiceField(
        required=False,
        queryset=Tipo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
#---------------------------------------------------------- Compras ----------------------------------------------------------

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['num_factura', 'fecha_compra', 'proveedor']
        
        widgets = {
            'num_factura': forms.TextInput(attrs={
                'placeholder': 'Ingrese el número de factura',
                'class': 'form-control'
            }),
            'fecha_compra': forms.DateInput(attrs={
                'placeholder': 'Ingrese la fecha de compra',
                'type': 'date',  # Cambiado a 'date' para que solo seleccione la fecha
                'class': 'form-control',
                'value': timezone.now().strftime('%Y-%m-%d')  # Fecha actual como valor por defecto
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

# ----------------------------Formulario para Detalle de Compras-----------------------------------------
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['num_factura', 'producto', 'cantidad', 'precio_unitario', 'iva']
        widgets = {
            'num_factura': forms.TextInput(attrs={
                'placeholder': 'Número de Factura',
                'class': 'form-control',
                'readonly': True  # Si no deseas que sea editable
            }),
            'producto': forms.Select(attrs={'placeholder': 'Seleccione el producto', 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad', 'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio', 'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'placeholder': 'Ingrese el IVA (%)', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.compra_id = kwargs.pop('compra_id', None)
        super().__init__(*args, **kwargs)
        # Si `compra_id` está presente, establecer el valor inicial para `num_factura`
        if self.compra_id:
            self.fields['num_factura'].initial = self.compra_id  # Aquí se establece el valor inicial

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get("cantidad")
        precio_unitario = cleaned_data.get("precio_unitario")

        if cantidad is not None and cantidad <= 0:
            self.add_error('cantidad', 'La cantidad debe ser mayor que 0.')

        if precio_unitario is not None and precio_unitario <= 0:
            self.add_error('precio_unitario', 'El precio unitario debe ser mayor que 0.')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.compra_id:
            # Obtener la instancia de `Compras` usando `num_factura` y asignarla
            instance.compra = get_object_or_404(Compras, num_factura=self.compra_id)
        if commit:
            instance.save()
        return instance
#-------------------------------- filtro de stok para que se filtre en rangos espesificos ---------------
class StockFilterForm(forms.Form):
    nombre_pro = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    cantidad_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    precio_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    precio_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )