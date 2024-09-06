from dataclasses import fields
from django.forms import ModelForm, TextInput, Select, DateTimeInput, NumberInput
from django import forms
from django_select2.forms import Select2Widget
from app.models import *
from django.forms import ModelForm
from django.core.exceptions import ValidationError

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
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['tipo_persona', 'nombres', 'razon_social', 'tipo_documento', 'numero_documento', 'correo', 'telefono', 'ciudad', 'direccion']

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')

        # Permitir el mismo número de documento si es la instancia actual (es decir, si se está editando)
        if Cliente.objects.exclude(pk=self.instance.pk).filter(numero_documento=numero_documento).exists():
            raise ValidationError("Ya existe una persona con ese número de documento.")
        
        return numero_documento

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional si es necesario
        return cleaned_data
#---------------------------------------------------------- Proveedor ----------------------------------------------------------
from django.core.exceptions import ValidationError

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

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')

        # Solo validar duplicado si no es la instancia actual
        if Proveedor.objects.exclude(pk=self.instance.pk).filter(numero_documento=numero_documento).exists():
            raise ValidationError("Ya existe un proveedor con este número de documento.")

        return numero_documento

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')

        # Solo validar duplicado si no es la instancia actual
        if Proveedor.objects.exclude(pk=self.instance.pk).filter(correo=correo).exists():
            raise ValidationError("Ya existe un proveedor con este correo electrónico.")

        return correo

    def clean(self):
        cleaned_data = super().clean()
        # Otras validaciones adicionales pueden ir aquí si es necesario
        return cleaned_data


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

#---------------------------------------------------------- Persona ----------------------------------------------------------
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['rol', 'nombres', 'tipo_documento','numero_documento', 'correo', 'telefono', 'usuario', 'password']
        widgets = {
            'rol': Select(
                attrs={
                    'placeholder': 'Seleccione el rol del usuario',
                }
            ),
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre completo del empleado',
                    'autofocus': 'autofocus',
                }
            ),
            'tipo_documento': Select(
                attrs={
                    'placeholder': 'Seleccione el tipo de documento',
                }
            ),
            'numero_documento': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de documento',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el correo electrónico',
                    'type': 'email',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de celular',
                    'type': 'tel',
                }
            ),
            'usuario': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de usuario',
                }
            ),
            'password': TextInput(
                attrs={
                    'placeholder': 'Ingrese la contraseña',
                    'type': 'password',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        numero_documento = cleaned_data.get('numero_documento')

        if Persona.objects.filter(correo=correo).exists():
            self.add_error('correo', 'Ya existe una persona con este correo electrónico.')

        if Persona.objects.filter(numero_documento=numero_documento).exists():
            self.add_error('numero_documento', 'Ya existe una persona con este número de documento.')

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
        self.fields['proveedor'].widget.attrs['autofocus'] = True
        self.fields['total'].widget.attrs['readonly'] = True

    class Meta:
        model = Compras
        fields = ['num_factura', 'fecha_compra', 'nombre_producto', 'cantidad', 'precio', 'iva', 'total', 'proveedor']
        widgets = {
            'num_factura': forms.TextInput(attrs={'placeholder': 'Ingrese el número de factura'}),
            'fecha_compra': forms.DateTimeInput(attrs={'placeholder': 'Ingrese la fecha de compra', 'type': 'datetime-local'}),
            'nombre_producto': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del producto'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio en céntimos'}),  # Indicar que es en céntimos
            'iva': forms.NumberInput(attrs={'placeholder': 'Ingrese el IVA (%)'}),
            'total': forms.NumberInput(attrs={'readonly': 'readonly'}),  # Campo total como solo lectura
            'proveedor': forms.Select(attrs={'autofocus': True}),
        }