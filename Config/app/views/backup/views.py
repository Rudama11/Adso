import os
import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
import subprocess

def backup_view(request):
    return render(request, 'backup.html')

def backup_database(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sql')

    try:
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        db_port = settings.DATABASES['default']['PORT']

        # Comando para hacer dump de la base de datos
        dump_command = [
            'mysqldump',
            f'--user={db_user}',
            f'--password={db_password}',
            f'--host={db_host}',
            f'--port={db_port}',
            db_name,
            f'--result-file={backup_file}'
        ]

        subprocess.run(dump_command, check=True)

        return JsonResponse({'status': 'success', 'message': 'Copia de seguridad creada exitosamente.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f"Error al crear la copia de seguridad: {e}"})

def restore_database(request):
    if request.method == 'POST' and request.FILES['backup_file']:
        backup_file = request.FILES['backup_file']

        try:
            db_name = settings.DATABASES['default']['NAME']
            db_user = settings.DATABASES['default']['USER']
            db_password = settings.DATABASES['default']['PASSWORD']
            db_host = settings.DATABASES['default']['HOST']
            db_port = settings.DATABASES['default']['PORT']

            # Guardar el archivo subido temporalmente
            temp_file_path = os.path.join(settings.BASE_DIR, 'temp_backup.sql')
            with open(temp_file_path, 'wb+') as destination:
                for chunk in backup_file.chunks():
                    destination.write(chunk)

            # Comando para restaurar la base de datos
            restore_command = [
                'mysql',
                f'--user={db_user}',
                f'--password={db_password}',
                f'--host={db_host}',
                f'--port={db_port}',
                db_name,
            ]

            with open(temp_file_path, 'rb') as input_file:
                process = subprocess.Popen(restore_command, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

            # Eliminar el archivo temporal
            os.remove(temp_file_path)

            if process.returncode == 0:
                return JsonResponse({'status': 'success', 'message': 'Base de datos restaurada exitosamente.'})
            else:
                return JsonResponse({'status': 'error', 'message': f"Error al restaurar la base de datos: {stderr.decode('utf-8')}"})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error al restaurar la base de datos: {e}"})
    else:
        return JsonResponse({'status': 'error', 'message': "Error al restaurar la base de datos."})