from dataclasses import fields
from django.forms import ModelForm, TextInput, Select, DateTimeInput, NumberInput
from django import forms
from django_select2.forms import Select2Widget
from app.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

#---------------------------------------------------------- Usuario ----------------------------------------------------------

# Formulario exclusivo para la creación de usuarios.
User = get_user_model()

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña nuevamente")
    email2 = forms.EmailField(label="Confirme nuevamente el correo")

    class Meta:
        model = User
        fields = ['username', 'nombres', 'email', 'email2', 'password']  # Orden de los campos

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_email2(self):
        email1 = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email1 and email2 and email1 != email2:
            raise ValidationError("Los correos electrónicos no coinciden")
        return email2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Establece la contraseña cifrada
        if commit:
            user.save()
        return user
    
# Formulario exclusivo para editar los usuarios.

class UsuarioEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False, label="Nueva Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, required=False, label="Confirmar Nueva Contraseña")
    email2 = forms.EmailField(required=False, label="Confirme nuevamente el correo")

    class Meta:
        model = User
        fields = ['username', 'nombres', 'email', 'email2', 'password', 'password2', 'is_active']  # Ajusta el orden de los campos

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 or password2:  # Solo valida si se ingresó alguna contraseña
            if password1 != password2:
                raise ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_email2(self):
        email1 = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email1 and email2 and email1 != email2:
            raise ValidationError("Los correos electrónicos no coinciden")
        return email2

    def save(self, commit=True):
        user = super().save(commit=False)
        # Solo actualiza la contraseña si se proporciona una nueva
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        
        # Actualiza el email solo si se proporciona un nuevo valor
        email = self.cleaned_data.get('email')
        if email:
            user.email = email

        # Marca al usuario como activo o inactivo
        user.is_active = self.cleaned_data.get('is_active', user.is_active)

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
class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['autofocus'] = True

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un numero de factura'
                }
            ),
        }

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
        self.fields['proveedor'].widget.attrs['autofocus'] = True
        self.fields['total'].widget.attrs['readonly'] = True
        # Establecer la fecha actual por defecto si no se ha proporcionado
        if not self.instance.pk:  # Solo si es una nueva instancia
            self.fields['fecha_compra'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M')

    class Meta:
        model = Compras
        fields = ['num_factura', 'fecha_compra', 'producto', 'cantidad', 'precio', 'iva', 'total', 'proveedor']
        widgets = {
            'num_factura': forms.TextInput(attrs={'placeholder': 'Ingrese el número de factura'}),
            'fecha_compra': forms.DateTimeInput(attrs={'placeholder': 'Ingrese la fecha de compra', 'type': 'datetime-local'}),
            'producto': forms.Select(attrs={'placeholder': 'Seleccione el producto'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio en céntimos'}),
            'iva': forms.NumberInput(attrs={'placeholder': 'Ingrese el IVA (%)'}),
            'total': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'proveedor': forms.Select(attrs={'autofocus': True}),
        }