import os
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import subprocess
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Vista para realizar el backup de la base de datos
@login_required
def backup_view(request):
    # Definir la ruta donde se almacenan los archivos de backup
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')

    archivos_backup = []
    if os.path.exists(backup_dir):
        # Obtener todos los archivos con extensión .sql en el directorio de backups
        for archivo in os.listdir(backup_dir):
            if archivo.endswith('.sql'):
                # Ruta completa del archivo
                archivo_path = os.path.join(backup_dir, archivo)
                # Obtener la fecha de creación del archivo
                timestamp = os.path.getctime(archivo_path)
                fecha_creacion = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Agregar a la lista como diccionario con el nombre del archivo y la fecha de creación
                archivos_backup.append({
                    'nombre': archivo,
                    'fecha_creacion': fecha_creacion
                })

        # Ordenarlos por fecha de creación, el más reciente primero
        archivos_backup.sort(key=lambda x: x['fecha_creacion'], reverse=True)

    # Pasar la lista de archivos al contexto de la plantilla
    contexto = {
        'archivos_backup': archivos_backup,
    }

    return render(request, 'backup.html', contexto)



@login_required  # Solo los usuarios autenticados pueden crear un backup
def backup_database(request):
    if request.method == 'POST':
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

            # Enviar respuesta JSON
            return JsonResponse({'status': 'success', 'message': 'Copia de seguridad creada exitosamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error al crear la copia de seguridad: {e}"})



@login_required  # Solo los usuarios autenticados pueden restaurar la base de datos
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def restore_database(request):
    if request.method == 'POST':
        # Obtener el nombre del archivo desde el formulario
        backup_file = request.POST.get('backup_file')

        # Validar que el archivo existe y tiene la extensión correcta
        backup_path = os.path.join(settings.BASE_DIR, 'backups', backup_file)
        if not os.path.exists(backup_path) or not backup_file.endswith('.sql'):
            return JsonResponse({'status': 'error', 'message': 'Archivo no encontrado o formato incorrecto.'})

        try:
            db_name = settings.DATABASES['default']['NAME']
            db_user = settings.DATABASES['default']['USER']
            db_password = settings.DATABASES['default']['PASSWORD']
            db_host = settings.DATABASES['default']['HOST']
            db_port = settings.DATABASES['default']['PORT']

            # Comando para restaurar la base de datos
            restore_command = [
                'mysql',
                f'--user={db_user}',
                f'--password={db_password}',
                f'--host={db_host}',
                f'--port={db_port}',
                db_name,
            ]

            # Abrir el archivo de backup seleccionado
            with open(backup_path, 'rb') as input_file:
                process = subprocess.Popen(restore_command, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

            if process.returncode == 0:
                return JsonResponse({'status': 'success', 'message': 'Base de datos restaurada exitosamente.'})
            else:
                return JsonResponse({'status': 'error', 'message': f"Error al restaurar la base de datos: {stderr.decode('utf-8')}"})


        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error al restaurar la base de datos: {e}"})
    else:
        return JsonResponse({'status': 'error', 'message': "Error al restaurar la base de datos."})



login_required  # Solo los usuarios autenticados pueden eliminar archivos
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def delete_backup(request):
    if request.method == 'POST':
        archivo = request.POST.get('archivo')
        backup_dir = os.path.join(settings.BASE_DIR, 'backups', archivo)

        try:
            if os.path.exists(backup_dir):
                os.remove(backup_dir)
                return JsonResponse({'status': 'success', 'message': 'Archivo eliminado exitosamente.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'El archivo no existe.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar el archivo: {e}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})