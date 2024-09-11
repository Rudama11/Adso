from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from app.models import CustomUser
from app.forms import UsuarioForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

class UsuarioCreateView(CreateView):
    model = CustomUser
    form_class = UsuarioForm
    template_name = 'usuario/crear.html'
    success_url = reverse_lazy('usuario_listar')


class UsuarioUpdateView(UpdateView):
    model = CustomUser
    form_class = UsuarioForm
    template_name = 'usuario/editar.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioDeleteView(DeleteView):
    model = CustomUser
    template_name = 'usuario/eliminar.html'
    success_url = reverse_lazy('usuario_listar')
