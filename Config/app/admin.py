from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Ubicacion)
admin.site.register(Tipo)