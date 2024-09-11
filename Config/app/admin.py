from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import CustomUser  # Asegúrate de que la importación del modelo sea correcta

# Registra los modelos existentes
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Compras)
admin.site.register(Normativa)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Tipo)
admin.site.register(Ubicacion)
admin.site.register(Venta)

# Configura el admin para el nuevo modelo CustomUser
class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
