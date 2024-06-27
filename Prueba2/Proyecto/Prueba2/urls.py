from django.contrib import admin
from django.urls import path,include
from apl.views import *
from inicio.views import *
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apl/', include('apl.urls')),
    path('',IndexView.as_view(), name='index'),
    path('login/', include('login.urls')),
]