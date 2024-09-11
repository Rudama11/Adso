from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from app.forms import UsuarioCreateForm,UsuarioChangeForm
from app.models import CustomUser

class UsuarioCreateView(CreateView):
    model = CustomUser
    form_class = UsuarioCreateForm
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('user_list')  # Redirige a la lista de usuarios después de crear un nuevo usuario

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Establece la contraseña cifrada
        user.save()
        return super().form_valid(form)
    
def register(request):
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirige a la página de perfil o cualquier otra página
    else:
        form = UsuarioCreateForm()
    return render(request, 'usuario/register.html', {'form': form})


def profile(request):
    return render(request, 'usuario/profile.html')

@login_required
class UsuarioUpdateView(UpdateView):
    model = CustomUser
    form_class = UsuarioChangeForm
    template_name = 'usuario/editar_usuario.html'
    success_url = reverse_lazy('user_list')

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')
        return get_object_or_404(CustomUser, id=user_id)

# Usando ListView para listar usuarios
class UserListView(ListView):
    model = CustomUser
    template_name = 'usuario/user_list.html'
    context_object_name = 'object_list'  # Esto asegura que se pase como object_list para la plantilla

    # Si deseas paginación, puedes agregar:
    paginate_by = 10  # Número de usuarios por página (opcional)

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'usuario/user_detail.html', {'user': user})

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'usuario/delete_user.html'
    success_url = reverse_lazy('app:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Usuario'
        context['entidad'] = 'Usuario'
        context['listar_url'] = reverse_lazy('app:user_list')
        return context