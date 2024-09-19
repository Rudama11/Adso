from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'nombres', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'nombres')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombres', 'email')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        # Si el usuario no es superusuario, deshabilitamos is_superuser en el admin
        if not request.user.is_superuser:
            form.base_fields['is_superuser'].disabled = True
        # Si el usuario no es superusuario o admin, deshabilitamos is_staff
        if not (request.user.is_superuser or request.user.is_staff):
            form.base_fields['is_staff'].disabled = True
        return form

    # Este método impide que un usuario no superusuario pueda ver o editar usuarios superusuarios
    def has_change_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
