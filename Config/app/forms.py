from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea
from django import forms
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

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del Proveedor'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
            'razon_social': forms.TextInput(attrs={'placeholder': 'Ingrese la razón social'}),
            'tipo_documento': forms.Select(attrs={'placeholder': 'Seleccione el tipo de documento'}),
            'numero_documento': forms.TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo'}),
            'telefono': forms.NumberInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'cod_postal': forms.Select(attrs={'placeholder': 'Ingrese la ubicación'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True
        if self.instance and self.instance.tipo_persona == 'PJ':
            self.fields['nombres'].widget.attrs['style'] = 'display:block;'
            self.fields['apellidos'].widget.attrs['style'] = 'display:block;'
            self.fields['razon_social'].widget.attrs['style'] = 'display:none;'
            self.fields['tipo_documento'].widget.attrs['style'] = 'display:block;'
            self.fields['numero_documento'].widget.attrs['style'] = 'display:block;'
        else:
            self.fields['razon_social'].widget.attrs['style'] = 'display:none;'
            self.fields['razon_social'].widget.attrs['style'] = 'display:block;'
            self.fields['tipo_documento'].widget.attrs['style'] = 'display:block;'
            self.fields['numero_documento'].widget.attrs['style'] = 'display:block;'

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
            'descripcion': TextInput(
            attrs={
                    'placeholder': 'Ingrese la descripcion ',
                    }
                ),
            'producto':forms.Select(
                attrs={
                    'placeholder': 'Seleccione el producto',
                    }
                ),
        }
        
#------------------------- ventas --------------------------------------------

from django import forms
from django.forms import ModelForm
from app.models import Venta

class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['autofocus'] = True

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(
                attrs={
                    'placeholder': 'Seleccione el cliente',
                }
            ),
            'fecha_ingreso': forms.DateInput(
                attrs={
                    'placeholder': 'Ingrese la fecha de ingreso',
                    'type': 'date'
                }
            ),
            'subtotal': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese el subtotal',
                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese el total',
                }
            ),
            'iva': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese el IVA',
                }
            ),
        }
