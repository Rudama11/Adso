from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario  # Asegúrate de que la importación sea correcta según la ubicación de tu modelo

@receiver(post_save, sender=User)
def create_or_update_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)
    else:
        instance.usuario.save()