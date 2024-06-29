from django.urls import path
from login.views import * 
from .views import LoginFormView, logoutredirect

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout', logoutredirect.as_view(), name='logout')
]