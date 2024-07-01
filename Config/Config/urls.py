from django.contrib import admin
from django.urls import path,include
from app.views import*
from inicio.views import IndexView
from login.views import *

urlpatterns = [
    path ('',IndexView.as_view(),name='index'),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('Prueba/',include ('app.urls'))                                                                                                                               
]