from django.contrib import admin
from django.urls import path,include
from app.views import*
from inicio.views import IndexView
from login.views import *
from dashboard.views import*
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index_pr'),
    path('dashboard', dashView.as_view(), name='dashboard'),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('app/',include ('app.urls')),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='register/password_reset_form.html'), name='password_reset'), 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'),name='password_reset_confirm'), 
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'),                                                                                                                              
]