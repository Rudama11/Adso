from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from app.models import *

#------------- Categoría ---------------------------------------------------

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True


    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre'
                    }
                ),
            'descripcion': Textarea(
            attrs={'placeholder': 'Ingrese la descripción',
                    'rows': 1,
                    'cols': 50
                    }
                    ),
        }
        
#------------- Ubicación ---------------------------------------------------

class UbicacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departamento'].widget.attrs['autofocus'] = True


    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'departamento': TextInput(
                attrs={
                    'placeholder': 'Ingrese el departamento'
                    }
                ),
            'ciudad': TextInput(
            attrs={
                    'placeholder': 'Ingrese la ciudad',
                    }
                ),
        }

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True


    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del cliente'
                    }
                ),
            'apellido': TextInput(
            attrs={
                    'placeholder': 'Ingrese el apellido del cliente',
                    }
                ),
        }
    
#------------- Proveedor ---------------------------------------------------

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del Proveedor'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
            'razon_social': forms.TextInput(attrs={'placeholder': 'Ingrese la razón social'}),
            'nit': forms.TextInput(attrs={'placeholder': 'Ingrese el NIT'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True
        # Inicialmente oculta los campos de Persona Jurídica
        if self.instance and self.instance.tipo_persona == 'PJ':
            self.fields['nombres'].widget.attrs['style'] = 'display:none;'
            self.fields['apellidos'].widget.attrs['style'] = 'display:none;'
        else:
            self.fields['razon_social'].widget.attrs['style'] = 'display:none;'
            self.fields['nit'].widget.attrs['style'] = 'display:none;'

class TipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del Tipo de producto'
                    }
                ),
            'descripcion': TextInput(
            attrs={
                    'placeholder': 'Ingrese la descripcion del Tipo',
                    }
                ),
        }

#------------- Producto ---------------------------------------------------
class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del producto'
                    }
                ),
            'descripcion': TextInput(
            attrs={
                    'placeholder': 'Ingrese la descripcion del producto',
                    }
                ),
        }