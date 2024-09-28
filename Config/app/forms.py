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
        fields = ['username', 'nombres', 'email', 'tipo_usuario']  # Incluye tipo_usuario en fields

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
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.initial_data = {
            'nombre': self.instance.nombre,
            'descripcion': self.instance.descripcion,
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')

        if nombre == self.initial_data['nombre'] and descripcion == self.initial_data['descripcion']:
            raise ValidationError("No se ha modificado ningún dato. Por favor, realice algún cambio antes de guardar.")

        return cleaned_data

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                    'rows': 1,
                    'cols': 50,
                    'class': 'form-control'
                }
            ),
        }

#---------------------------------------------------------- Tipo ----------------------------------------------------------

class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Ingrese el nombre del Tipo de producto',
            'class': 'form-control'
        })
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Ingrese la descripción del Tipo',
            'class': 'form-control'
        })
        self.initial_data = {
            'nombre': self.instance.nombre,
            'descripcion': self.instance.descripcion,
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')

        if nombre == self.initial_data['nombre'] and descripcion == self.initial_data['descripcion']:
            raise ValidationError("No se ha modificado ningún dato. Por favor, realice algún cambio antes de guardar.")

        return cleaned_data

    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del Tipo de producto'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la descripción del Tipo de producto'
                }
            ),
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
    class Meta:
        model = Cliente
        fields = ['tipo_persona', 'nombres', 'razon_social', 'tipo_documento', 'numero_documento', 'correo', 'telefono', 'ciudad', 'direccion']

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        # Verificamos si estamos en el modo de edición (si existe una instancia)
        if self.instance and self.instance.pk:
            # Si estamos editando, verificamos que el número de documento no exista en otro cliente
            if Cliente.objects.exclude(pk=self.instance.pk).filter(numero_documento=numero_documento).exists():
                raise ValidationError("Ya existe una persona con ese número de documento.")
        else:
            # Si estamos creando uno nuevo, verificamos que no exista ya el número de documento
            if Cliente.objects.filter(numero_documento=numero_documento).exists():
                raise ValidationError("Ya existe una persona con ese número de documento.")
        return numero_documento

    def clean(self):
        cleaned_data = super().clean()
        # Puedes añadir más validaciones si es necesario
        return cleaned_data
#---------------------------------------------------------- Proveedor ----------------------------------------------------------
from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del Proveedor'}),
            'razon_social': forms.TextInput(attrs={'placeholder': 'Ingrese la razón social'}),
            'tipo_documento': forms.Select(attrs={'placeholder': 'Seleccione el tipo de documento'}),
            'numero_documento': forms.TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'ciudad': forms.Select(attrs={'placeholder': 'Ingrese la ubicación'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        numero_documento = cleaned_data.get('numero_documento')

        # Validación para correo, ignorando la instancia actual
        if Proveedor.objects.exclude(pk=self.instance.pk).filter(correo=correo).exists():
            self.add_error('correo', 'Ya existe una persona con este correo electrónico.')

        # Validación para número de documento, ignorando la instancia actual
        if Proveedor.objects.exclude(pk=self.instance.pk).filter(numero_documento=numero_documento).exists():
            self.add_error('numero_documento', 'Ya existe una persona con este número de documento.')

        return cleaned_data


#--------------------------------------------------------- Producto ----------------------------------------------------------
class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({
            'autofocus': True,
            'placeholder': 'Ingrese el nombre del producto',
            'class': 'form-control'
        })
        self.fields['categoria'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['tipo_pro'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'tipo_pro']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pro': forms.Select(attrs={'class': 'form-control'}),
        }

#------------------------------------------------------- Normativa----------------------------------------------------------
class NormativaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['decreto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Normativa
        fields = '__all__'
        widgets = {
            'decreto': TextInput(
                attrs={
                    'placeholder': 'Ingrese la normativa',
                    'class': 'form-control'
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                    'class': 'form-control'
                }
            ),
            'producto': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
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
                    'class': 'form-control'  # Puedes añadir clases CSS para estilizar
                }
            ),
            'fecha_emision': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Seleccione la fecha de emisión',
                    'class': 'form-control',
                    'type': 'datetime-local'  # Permite seleccionar fecha y hora
                }
            ),
            'cliente': forms.Select(
                attrs={
                    'class': 'form-control'  # Para estilizar el select
                }
            ),
        }
        
        
#---------------------------------------------------------- Dellate  Ventas---------------------------------------------------------------
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad', 'iva', 'total', 'precio', 'num_factura']
        widgets = {
            'venta': forms.Select(attrs={'class': 'form-control', 'id': 'id_venta'}),
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
#---------------------------------------------------------- Producto Filter Form ----------------------------------------------------------
class ProductoFilterForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'class': 'form-control'})
    )
    descripcion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Descripción del producto', 'class': 'form-control'})
    )
    stock_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Stock mínimo', 'class': 'form-control'})
    )
    stock_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Stock máximo', 'class': 'form-control'})
    )
    precio_min = forms.DecimalField(
        required=False,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'placeholder': 'Precio mínimo', 'class': 'form-control'})
    )
    precio_max = forms.DecimalField(
        required=False,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'placeholder': 'Precio máximo', 'class': 'form-control'})
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
            self.fields['fecha_compra'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M')

    class Meta:
        model = Compras
        fields = ['num_factura', 'fecha_compra', 'proveedor']
        
        widgets = {
            'num_factura': forms.TextInput(attrs={
                'placeholder': 'Ingrese el número de factura',
                'class': 'form-control'
            }),
            'fecha_compra': forms.DateTimeInput(attrs={
                'placeholder': 'Ingrese la fecha de compra',
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

#------------------------------- detalle Compra----------------------------

from django import forms
from django.shortcuts import get_object_or_404
from .models import DetalleCompra, Compras

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