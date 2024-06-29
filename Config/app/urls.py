from django.urls import path
from app.views import*
from app.views.Categoria.views import *

# Define el namespace para la aplicación

app_name = 'app'

urlpatterns = [
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'), 
    path('categoria/listar2/', lista_categoria, name='categoria_lista2' ),
    # path('uno/', Vista1, name='Vista1'),
    # path('dos/', Vista2, name='Vista2'),  # Corregido el nombre a 'Vi44sta2'
]
