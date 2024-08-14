from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, DecimalField
from django import forms
from django_select2.forms import Select2Widget
from app.models import *

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
                attrs={
                    'placeholder': 'Ingrese la descripción',
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
        self.fields['nombre'].widget.attrs['autofocus'] = True
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

#------------------------- ventas --------------------------------------------

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