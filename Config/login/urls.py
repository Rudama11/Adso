# from django.urls import path
# from login.views import * 
# from .views import LoginFormView, logoutredirect

# urlpatterns = [
#     path('', LoginFormView.as_view(), name='login'),
#     path('logout', logoutredirect.as_view(), name='logout')
    
# ]
from django.urls import path
from .views import LoginFormView, logoutredirect, UserEmailValidationView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout', logoutredirect.as_view(), name='logout'),
    path('check-email/', UserEmailValidationView.as_view(), name='check_email'),  # Ruta para la validación del correo electrónico
]

