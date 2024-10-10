from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class CustomLoginRequiredMixin(LoginRequiredMixin, View):
    """
    Clase base global que aplica login_required a todas las vistas que hereden de ella.
    """
    pass