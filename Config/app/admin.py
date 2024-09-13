from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import CustomUser
from app.forms import UsuarioForm, UsuarioEditForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = UsuarioForm  # Usamos tu formulario para la creación de usuarios
    form = UsuarioEditForm  # Usamos tu formulario para la edición de usuarios
    model = CustomUser
    list_display = ('username', 'email', 'nombres', 'tipo_usuario', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'tipo_usuario')  # Agrega 'tipo_usuario' al filtro
    search_fields = ('username', 'email', 'nombres')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombres', 'email', 'tipo_usuario')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombres', 'password', 'password2', 'tipo_usuario', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)