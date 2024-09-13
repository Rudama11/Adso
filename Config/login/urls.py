from django.urls import path
from .views import LoginFormView, logoutredirect, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', logoutredirect.as_view(), name='logout'),
    path('Restablece_Contrasena/', PasswordResetView.as_view(), name='Restablece_Contrasena'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]