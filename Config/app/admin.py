from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import CustomUser
from app.forms import UsuarioForm, UsuarioEditForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = UsuarioForm
    form = UsuarioEditForm
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

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombres', 'password', 'password2', 'is_staff', 'is_active')}
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si estamos editando un usuario existente
            if request.user.is_superuser:
                return self.readonly_fields
            else:
                return ('username', 'last_login', 'is_superuser', 'is_staff')
        return self.readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_staff=True)

    def save_model(self, request, obj, form, change):
        if not change:  # Si estamos creando un nuevo usuario
            if not request.user.is_superuser:
                obj.is_staff = True  # Asegúrate de que el admin tenga permisos de staff
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
