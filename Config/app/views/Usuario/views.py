from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import CustomUser
from app.forms import UsuarioForm,UsuarioEditForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@login_required
def perfil_view(request):
    user = request.user
    last_login = user.last_login
    context = {
        'last_login': last_login,
    }
    return render(request, 'perfil.html', context)

class UsuarioListView(ListView):
    model = CustomUser
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
    model = CustomUser
    form_class = UsuarioForm
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

class UsuarioUpdateView(UpdateView):
    model = CustomUser
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
    model = CustomUser
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
