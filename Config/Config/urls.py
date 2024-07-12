from django.contrib import admin
from django.urls import path,include
from app.views import*
from inicio.views import IndexView
from login.views import *
from dashboard.views import*

urlpatterns = [
    path('', IndexView.as_view(), name='index_pr'),
    path('dashboard', dashView.as_view(), name='dashboard'),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('app/',include ('app.urls'))                                                                                                                               
]