from django.urls import path
from apl.views import *
from apl.views.categoria.views import *

app_name = 'apl'
urlpatterns = [
    # path('categoria/listar2/', lista_categoria, name='categoria_lista2'  ),
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'  ),
    path('categoria/editar/<int:pk>/', CtegoriaUpdateView.as_view, name='categoria_editar'  ),
    
    # path('dos'/,vista2, name='vista2)
]