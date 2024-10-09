from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import CustomUser
from app.forms import UsuarioForm, UsuarioEditForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

class UsuarioListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'Usuario/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['entidad'] = 'Usuario'
        context['crear_url'] = reverse_lazy('app:usuario_crear')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

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

class UsuarioCreateView(CreateView):
    model = CustomUser
    form_class = UsuarioForm
    template_name = 'Usuario/crear.html'
    success_url = reverse_lazy('app:usuario_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
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

from django.contrib.auth.hashers import make_password

class UsuarioUpdateView(UpdateView):
    model = CustomUser
    form_class = UsuarioEditForm
    template_name = 'Usuario/editar.html'
    success_url = reverse_lazy('app:usuario_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:usuario_listar')
        return context

    def form_valid(self, form):
        # Solo actualiza la contraseña si se proporciona una nueva
        password = form.cleaned_data.get('password')
        if password:
            form.instance.password = make_password(password)  # Encriptar y guardar la nueva contraseña
        else:
            # Si no se proporciona una nueva contraseña, mantenemos la contraseña actual
            form.instance.password = self.get_object().password
        
        form.save()  # Guardar el resto del formulario
        return JsonResponse({
            'success': True,
            'message': 'Usuario actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

