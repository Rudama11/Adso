from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import CustomUser
from app.forms import UsuarioForm, UsuarioEditForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from functools import wraps
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password

# Decorador que verifica si el usuario es admin o superuser
def user_is_admin_or_superuser(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:  # Verificar si está autenticado
            if request.user.tipo_usuario in ['admin', 'superuser']:  # Solo permitir admin y superuser
                return view_func(request, *args, **kwargs)
            return redirect('app:acceso_denegado')  # Redirigir si no tiene permiso
        return redirect('login')  # Redirigir al login si no está autenticado
    return _wrapped_view

# Aplicar decoradores a la vista
@method_decorator(user_is_admin_or_superuser, name='dispatch')
class UsuarioListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'Usuario/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['entidad'] = 'Usuario'
        context['crear_url'] = reverse_lazy('app:usuario_crear')
         # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Usuario', 'url': reverse_lazy('app:usuario_listar')},
        ]
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar en función del tipo de usuario
        user = self.request.user

        # Si el usuario es 'admin', no podrá ver a los 'superuser'
        if user.tipo_usuario == 'admin':
            queryset = queryset.exclude(tipo_usuario='superuser')

        # Agregar filtros por username y email si están en los parámetros GET
        username = self.request.GET.get('username')
        email = self.request.GET.get('email')

        if username:
            queryset = queryset.filter(username__icontains=username)
        if email:
            queryset = queryset.filter(email__icontains=email)

        return queryset
    
    def EliminarUsuario(request, id_usuario):
        usuario = CustomUser.objects.get(pk=id_usuario)
        usuario.delete()
        return redirect('app:usuario_listar')

@method_decorator(user_is_admin_or_superuser, name='dispatch')
class UsuarioCreateView(LoginRequiredMixin,CreateView):
    model = CustomUser
    form_class = UsuarioForm
    template_name = 'Usuario/crear.html'
    success_url = reverse_lazy('app:usuario_listar')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Pasar el usuario autenticado al formulario
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
          # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Usuario', 'url': reverse_lazy('app:usuario_listar')},
            {'nombre': 'Crear Usuario', 'url': reverse_lazy('app:usuario_crear')},
        ]
        
        return context


    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Usuario creado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

@method_decorator(user_is_admin_or_superuser, name='dispatch')
class UsuarioUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    form_class = UsuarioEditForm
    template_name = 'Usuario/editar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario autenticado al formulario
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
       # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Usuario', 'url': reverse_lazy('app:usuario_listar')},
            {'nombre': 'Editar Usuario', 'url': reverse_lazy('app:usuario_editar', args=[self.object.pk])},
        ]

        return context

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        if password:
            form.instance.password = make_password(password)
        else:
            form.instance.password = self.get_object().password

        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Usuario actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)