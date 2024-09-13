from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from app.models import Usuario
from app.forms import UsuarioForm,UsuarioEditForm

class UsuarioListView(ListView):
    model = Usuario  # Cambia a Usuario
    template_name = 'usuario/listar.html'
    context_object_name = 'usuarios'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['entidad'] = 'Usuario'
        context['crear_url'] = reverse_lazy('app:usuario_crear')
        return context

class UsuarioCreateView(CreateView):
    model = Usuario  # Cambia a Usuario
    form_class = UsuarioForm  # Asegúrate de que este formulario exista y esté bien definido
    template_name = 'usuario/crear.html'
    success_url = reverse_lazy('app:usuario_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context

# app/views.py

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from app.forms import UsuarioEditForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioEditForm
    template_name = 'usuario/editar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def form_valid(self, form):
        user = form.save(commit=False)

        # Verifica si la contraseña ha sido cambiada
        if form.cleaned_data.get('password'):
            # Marcar al usuario como no autenticado (forzando un nuevo inicio de sesión)
            self.request.session.flush()
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

class UsuarioDeleteView(DeleteView):
    model = Usuario  # Cambia a Usuario
    template_name = 'usuario/eliminar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Usuario eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context