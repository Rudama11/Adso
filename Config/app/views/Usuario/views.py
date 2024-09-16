from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import CustomUser
from app.forms import UsuarioForm, UsuarioEditForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

@login_required
def perfil_view(request):
    user = request.user
    last_login = user.last_login
    context = {
        'last_login': last_login,
    }
    return render(request, 'perfil.html', context)

class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'usuario/listar.html'
    context_object_name = 'usuarios'

    def test_func(self):
        # Permitir acceso a superusuarios o usuarios con rol de administrador
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['entidad'] = 'Usuario'
        context['crear_url'] = reverse_lazy('app:usuario_crear')
        return context

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para acceder a esta página.')
        return redirect('app:acceso_denegado')

class UsuarioCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = UsuarioForm
    template_name = 'usuario/crear.html'
    success_url = reverse_lazy('app:usuario_listar')

    def test_func(self):
        # Permitir acceso a superusuarios o usuarios con rol de administrador
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para acceder a esta página.')
        return redirect('app:acceso_denegado')

class UsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UsuarioEditForm
    template_name = 'usuario/editar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def test_func(self):
        # Permitir acceso a superusuarios o usuarios con rol de administrador
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        user = form.save(commit=False)

        # Verifica si la contraseña ha sido cambiada
        if form.cleaned_data.get('password'):
            self.request.session.flush()  # Forzar cierre de sesión si la contraseña cambia
            messages.success(self.request, 'Contraseña cambiada exitosamente. Por favor, inicie sesión de nuevo.')
        
        user.save()
        messages.success(self.request, 'Usuario actualizado exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para acceder a esta página.')
        return redirect('app:acceso_denegado')

class UsuarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'usuario/eliminar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def test_func(self):
        # Permitir acceso a superusuarios o usuarios con rol de administrador
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para acceder a esta página.')
        return redirect('app:acceso_denegado')

def acceso_denegado_view(request):
    return render(request, 'acceso_denegado.html', {})
