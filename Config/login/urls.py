from django.urls import path
from login.views import * 
from .views import LoginFormView, logoutredirect,PasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout', logoutredirect.as_view(), name='logout'),
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),

    
]
