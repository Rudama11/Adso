from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea

from app.models import *

#Clase Categoria

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
        
#CLase Ubicacion

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
    
#Proveedor

class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del Proveedor'
                    }
                ),
            'apellidos': TextInput(
            attrs={
                    'placeholder': 'Ingrese el apellido',
                    }
                ),
        }

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

#------------------------- normativa --------------------------------------------

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
                    }
                ),
            'detalles': TextInput(
            attrs={
                    'placeholder': 'Ingrese la descripcion ',
                    }
                ),
        }