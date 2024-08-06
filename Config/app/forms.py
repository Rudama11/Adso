from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea, Select
from django import forms
from app.models import *
from django_select2.forms import Select2Widget

#---------------------------------------------------------- Categoria ----------------------------------------------------------

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

#---------------------------------------------------------- Tipo ----------------------------------------------------------

class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        # Agregar estilos y placeholders a los campos
        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Ingrese el nombre del Tipo de producto',
            'class': 'form-control'
        })
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Ingrese la descripción del Tipo',
            'class': 'form-control'
        })

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
                    'placeholder': 'Ingrese la descripción del Tipo de producto'
                }
            ),
        }
        
#---------------------------------------------------------- Ubicacion ----------------------------------------------------------
class UbicacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departamento'].widget.attrs.update({
            'class': 'select2',
            'placeholder': 'Seleccione el departamento'
        })
        self.fields['ciudad'].widget.attrs.update({
            'class': 'select2',
            'placeholder': 'Seleccione la ciudad'
        })

    class Meta:
        model = Ubicacion
        fields = ['departamento', 'ciudad']
        widgets = {
            'departamento': forms.Select(attrs={'class': 'select2'}),
            'ciudad': forms.Select(attrs={'class': 'select2'}),
        }

#---------------------------------------------------------- Cliente ----------------------------------------------------------
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del cliente'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
            'razon_social': forms.TextInput(attrs={'placeholder': 'Ingrese la razón social del cliente'}),
            'tipo_documento': forms.Select(attrs={'placeholder': 'Seleccione el tipo de documento'}),
            'numero_documento': forms.TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo'}),
            'telefono': forms.NumberInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'ciudad': forms.Select(attrs={'placeholder': 'Ingrese la ubicación'}),
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
            
#---------------------------------------------------------- Proveedor ----------------------------------------------------------

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
            'ciudad': forms.Select(attrs={'placeholder': 'Ingrese la ubicación'}),
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


#---------------------------------------------------------- Producto ----------------------------------------------------------
class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar autofocus al campo nombre
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
        # Agregar estilos y placeholders a los campos
        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Ingrese el nombre del producto',
            'class': 'form-control'
        })
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Ingrese la descripción del producto',
            'class': 'form-control'
        })
        self.fields['stock'].widget.attrs.update({
            'placeholder': 'Ingrese el stock del producto',
            'class': 'form-control'
        })
        self.fields['precio'].widget.attrs.update({
            'placeholder': 'Ingrese el precio del producto',
            'class': 'form-control'
        })
        self.fields['categoria'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['tipo_pro'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['venta'].widget.attrs.update({
            'class': 'form-control'
        })
    
    class Meta:
        model = Producto
        fields = '__all__'

#---------------------------------------------------------- Normativa ----------------------------------------------------------
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
                    'class': 'form-control'  # Agregar clase para estilos consistentes
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
                    'class': 'form-control'  # Agregar clase para estilos consistentes
                }
            ),
        }

#------------------------- ventas --------------------------------------------
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
            'fecha_emision': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ingrese la fecha de emisión',
                    'type': 'datetime-local'
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
            'impuestos': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese los impuestos',
                }
            ),
            'persona': forms.Select(
                attrs={
                    'placeholder': 'Seleccione la persona',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                }
            ),
        }

#------------------------- Persona --------------------------------------------
class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del empleado',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido del empleado',
                }
            ),
            'cedula': TextInput(
                attrs={
                    'placeholder': 'Ingrese la cedula del empleado',
                }
            ),
            'fecha_registro': forms.DateInput(
                attrs={
                    'placeholder': 'Ingrese la fecha de registro',
                    'type': 'date'
                }
            ),
            'edad': TextInput(
                attrs={
                    'placeholder': 'Ingrese la edad del empleado',
                }
            ),
            'salario': TextInput(
                attrs={
                    'placeholder': 'Ingrese el salario del empleado',
                }
            ),
            'estado': Select(
                attrs={
                    'placeholder': 'Seleccione el estado del empleado',
                }
            ),
            'tipo': Select(
                attrs={
                    'placeholder': 'Seleccione el tipo de empleado',
                }
            ),
            'categ': Select(
                attrs={
                    'placeholder': 'Seleccione la categoría del empleado',
                }
            ),
        }
