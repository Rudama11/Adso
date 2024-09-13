# app/admin.py
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombres', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'nombres')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-last_login',)
