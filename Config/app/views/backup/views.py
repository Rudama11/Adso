# app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import os
import sqlite3
from django.conf import settings

def backup_database(request):
    # Definir la ruta y nombre del archivo de copia de seguridad
    backup_file = os.path.join(settings.BASE_DIR, 'backup.sqlite3')

    # Conectar a la base de datos actual
    conn = sqlite3.connect(os.path.join(settings.BASE_DIR, 'db.sqlite3'))
    with open(backup_file, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()

    return HttpResponse("Copia de seguridad creada exitosamente.")

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

def backup_view(request):
    return render(request, 'backup.html')