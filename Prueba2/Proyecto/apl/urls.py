from django.urls import path
from apl.views import *
from apl.views.categoria.views import *

app_name = 'apl'
urlpatterns = [
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'  ),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'  ),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'),
]