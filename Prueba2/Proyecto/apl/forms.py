from dataclasses import fields
from django.forms import ModelForm

from apl.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'