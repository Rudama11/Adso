from django.utils.timezone import localtime
from app.models import CustomUser

def user_last_login(request):
    if request.user.is_authenticated:
        last_login = localtime(request.user.last_login)  # Convierte a la hora local
    else:
        last_login = None
    return {
        'last_login': last_login,
    }

def user_count(request):
    user_count = CustomUser.objects.count()
    return {
        'user_count': user_count,
    }

def user_name(request):
    if request.user.is_authenticated:
        user_name = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    else:
        user_name = None
    return {
        'user_name': user_name,
    }