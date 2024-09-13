from django.utils.timezone import now

def user_last_login(request):
    if request.user.is_authenticated:
        return {'user_last_login': request.user.last_login}
    return {'user_last_login': None}

from django.contrib.auth import get_user_model

def user_count(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual
    return {'user_count': User.objects.count()}
