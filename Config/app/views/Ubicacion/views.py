import django
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from app.models import Ubicacion


def lista_ubicacion(request):
    Nombre = {
        
    'titulo': 'Listado de ubicacion',
    'ubicacion': Ubicacion.objects.all()
    }
    
    return render(request, 'Ubicacion/listarU.html', Nombre)

class UbicacionListView(ListView):
    model= Ubicacion
    template_name = 'Ubicacion/listarU.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,*args, **kwargs):
        Nombre ={'Nombre': 'Lorena'}
        return JsonResponse(Nombre)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicacion'
        return context
