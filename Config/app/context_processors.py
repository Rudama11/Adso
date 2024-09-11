from django.utils.timezone import localtime

def user_last_login(request):
    if request.user.is_authenticated:
        last_login = localtime(request.user.last_login)  # Convierte a la hora local
    else:
        last_login = None
    return {
        'last_login': last_login,
    }