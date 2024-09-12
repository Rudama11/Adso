from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import CustomUser
from app.forms import UsuarioForm  # Importamos tu UsuarioForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = UsuarioForm  # Usamos tu formulario para la creación de usuarios
    form = UsuarioForm  # También podemos usarlo para la edición de usuarios si lo deseas
    model = CustomUser
    list_display = ('username', 'email', 'nombres', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'nombres')
    ordering = ('username',)

    # Campos que se muestran al editar un usuario existente
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombres', 'email')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )

    # Campos que se muestran al crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombres', 'password', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)