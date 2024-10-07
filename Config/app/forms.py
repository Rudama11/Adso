from dataclasses import fields
from django.forms import ModelForm, TextInput, Select, DateTimeInput, NumberInput
from django import forms
from django_select2.forms import Select2Widget
from app.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404


#---------------------------------------------------------- Usuario ----------------------------------------------------------

# Formulario exclusivo para la creación de usuarios.
class UsuarioForm(forms.ModelForm):
    TIPO_USUARIO_CHOICES = [
        ('admin', 'Administrador'),
        ('usuario', 'Usuario normal'),
    ]
    
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES, label='Tipo de usuario')
    
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Nueva contraseña',
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*+]).{8,20}$',
                message=(
                    'La contraseña debe tener entre 8 y 20 caracteres, '
                    'incluyendo al menos una letra mayúscula, una letra minúscula, '
                    'un número y un carácter especial.'
                ),
            )
        ]
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirma nueva contraseña'
    )

    class Meta:
        model = CustomUser
        fields = ['tipo_usuario','username', 'nombres', 'email', 'password', ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Las contraseñas no coinciden.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        # Asignar permisos según el tipo de usuario seleccionado
        tipo_usuario = self.cleaned_data.get('tipo_usuario')
        
        if tipo_usuario == 'admin':
            user.is_staff = True  # Los administradores tienen permisos de staff
            user.is_superuser = False  # Los administradores tienen permisos de superusuario
        else:
            user.is_staff = False  # Los usuarios normales no tienen permisos de staff
            user.is_superuser = False

        if commit:
            user.save()
        return user

# Formulario exclusivo para editar los usuarios.

class UsuarioEditForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Nueva contraseña',
        required=False,  # No es obligatorio en el formulario de edición
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*+]).{8,20}$',
                message=(
                    'La contraseña debe tener entre 8 y 20 caracteres, '
                    'incluyendo al menos una letra mayúscula, una letra minúscula, '
                    'un número y un carácter especial.'
                ),
            )
        ]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirma nueva contraseña',
        required=False  # No es obligatorio en el formulario de edición
    )

    class Meta:
        model = CustomUser
        fields = ['tipo_usuario','username', 'nombres', 'email']  # Incluye tipo_usuario en fields

    def __init__(self, *args, **kwargs):
        # Obtenemos el usuario actual que edita
        self.current_user = kwargs.pop('user', None)
        super(UsuarioEditForm, self).__init__(*args, **kwargs)

        # Desactivar los campos de superusuario y staff si el usuario actual no tiene permisos
        if not self.current_user or not self.current_user.is_superuser:
            self.fields.pop('is_superuser', None)
        if not self.current_user or not (self.current_user.is_superuser or self.current_user.is_staff):
            self.fields.pop('is_staff', None)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Si el usuario ha proporcionado una nueva contraseña, asegúrate de que coincidan
        if password or password2:
            if password != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Solo actualiza la contraseña si el campo de contraseña no está vacío
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        else:
            # No hacer nada con la contraseña si no se ha proporcionado
            user.password = self.instance.password

        tipo_usuario = self.cleaned_data.get('tipo_usuario')

        # Asigna permisos según el tipo de usuario
        if tipo_usuario == 'admin':
            user.is_staff = True  # Los administradores tienen permisos de staff
            user.is_superuser = False  # Los administradores no tienen permisos de superusuario
        elif tipo_usuario == 'superadmin':
            user.is_superuser = True  # El superusuario tiene permisos de superusuario
            user.is_staff = True  # También tiene permisos de staff
        else:
            user.is_staff = False  # Los usuarios normales no tienen permisos de staff
            user.is_superuser = False

        if commit:
            user.save()
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Establecer enfoque automático en el campo proveedor
        self.fields['proveedor'].widget.attrs['autofocus'] = True
        
        # Establecer la fecha actual por defecto si es una nueva instancia
        if not self.instance.pk:  # Solo si es una nueva instancia
            self.fields['fecha_compra'].initial = timezone.now().strftime('%Y-%m-%d')  # Solo la fecha

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
                'class': 'form-control'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

#------------------------------- Detalle Compras ----------------------------

class DetalleCompraForm(forms.ModelForm):
    num_factura = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Número de Factura'})
        # Elimina 'disabled=True' para que el campo sea editable
    )

    class Meta:
        model = DetalleCompra
        fields = ['num_factura', 'producto', 'cantidad', 'precio_unitario', 'iva']
        widgets = {
            'producto': forms.Select(attrs={'placeholder': 'Seleccione el producto'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'precio_unitario': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio'}),
            'iva': forms.NumberInput(attrs={'placeholder': 'Ingrese el IVA (%)'}),
        }

    def __init__(self, *args, **kwargs):
        # Extraer `compra_id` del diccionario de argumentos
        self.compra_id = kwargs.pop('compra_id', None)
        super().__init__(*args, **kwargs)
        # Si `compra_id` está presente, establecer el valor inicial para `num_factura`
        if self.compra_id:
            self.fields['num_factura'].initial = self.compra_id

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.compra_id:
            # Obtener la instancia de `Compras` usando `num_factura` y asignarla
            instance.compra = get_object_or_404(Compras, num_factura=self.compra_id)
        if commit:
            instance.save()
        return instance