from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Ubicacion,Departamentos,Municipios
from app.forms import UbicacionForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST

class UbicacionListView(ListView):
    model = Ubicacion
    template_name = 'Ubicacion/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicaciones'
        context['entidad'] = 'Ubicacion'
        context['crear_url'] = reverse_lazy('app:ubicacion_crear')
        context['departamentos'] = Departamentos.objects.all()
        context['municipios'] = Municipios.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        departamento_id = self.request.GET.get('departamento')
        municipio_id = self.request.GET.get('municipio')

        if departamento_id:
            queryset = queryset.filter(departamento_id=departamento_id)
        if municipio_id:
            queryset = queryset.filter(municipio_id=municipio_id)

        return queryset
        
    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarUbicacion(request, id_ubica):
        try:
            ubica = get_object_or_404(Ubicacion, pk=id_ubica)
            ubica.delete()
            return JsonResponse({'status': 'success', 'message': 'Ubicacion eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/crear.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if form.non_field_errors():
            print("Error no relacionado con los campos: ", form.non_field_errors())
        return response

class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/editarUbi.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Ubicación'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listar')
        return context

def municipios_por_departamento(request):
    departamento_id = request.GET.get('departamento_id')
    if departamento_id:
        municipios = Municipios.objects.filter(departamento_id=departamento_id).values('id', 'nombre')
    else:
        municipios = []
    return JsonResponse({'municipios': list(municipios)})