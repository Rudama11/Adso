import os
import shutil
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

def backup_view(request):
    # Agregar un mensaje de éxito si se envió un backup correctamente
    if 'backup_success' in request.GET:
        messages.success(request, "Copia de seguridad creada exitosamente.")
    return render(request, 'backup.html')

def backup_database(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')  # Ruta de la carpeta backups
    os.makedirs(backup_dir, exist_ok=True)  # Crear la carpeta si no existe

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sqlite3')

    try:
        shutil.copy(os.path.join(settings.BASE_DIR, 'db.sqlite3'), backup_file)
        # Redirigir a la vista de backup y mostrar un mensaje de éxito
        return redirect('app:backup')  # Asegúrate de que el nombre sea correcto
    except Exception as e:
        return HttpResponse(f"Error al crear la copia de seguridad: {e}")

def restore_database(request):
    if request.method == 'POST' and request.FILES['backup_file']:
        backup_file = request.FILES['backup_file']

        # Definir la ruta de la base de datos actual
        db_file = os.path.join(settings.BASE_DIR, 'db.sqlite3')

        # Guardar la copia de seguridad cargada
        with open(db_file, 'wb+') as destination:
            for chunk in backup_file.chunks():
                destination.write(chunk)

        return HttpResponse("Base de datos restaurada exitosamente.")
    else:
        return HttpResponse("Error al restaurar la base de datos.")