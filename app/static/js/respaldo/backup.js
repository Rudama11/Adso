document.addEventListener('DOMContentLoaded', function() {
    const backupForm = document.getElementById('backup-form');
    const restoreForm = document.getElementById('restore-form');
    const fileInput = document.getElementById('backup-file-input');
    const fileNameDisplay = document.getElementById('file-name');
    const selectFileButton = document.getElementById('select-file-button');

    // Mostrar el cuadro de diálogo de selección de archivo al hacer clic en el botón
    selectFileButton.addEventListener('click', function() {
        fileInput.click();
    });

    // Actualizar el nombre del archivo seleccionado y validar la extensión
    fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        const fileName = file ? file.name : 'Sin archivos seleccionados';
        fileNameDisplay.textContent = fileName;

        // Validar la extensión del archivo
        const validExtensions = ['sql'];
        const fileExtension = fileName.split('.').pop().toLowerCase();

        if (!validExtensions.includes(fileExtension)) {
            Swal.fire({
                icon: 'error',
                title: 'Archivo inválido',
                text: 'Por favor, seleccione un archivo .sql'
            });
            fileInput.value = ''; // Limpiar el input si el archivo no es válido
            fileNameDisplay.textContent = 'Sin archivos seleccionados'; // Resetear el nombre mostrado
        }
    });

    // Manejar el envío del formulario de backup (Crear backup)
    backupForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(backupForm);

        fetch(backupUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                Swal.fire({
                    icon: 'success',
                    title: 'Éxito',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 1500
                }).then(() => {
                    location.reload();  // Recargar la página después del éxito
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: data.message
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al realizar la solicitud.'
            });
        });
    });

    // Manejar el envío del formulario de restauración (Restaurar backup)
    restoreForm.addEventListener('submit', function(e) {
        const fileName = fileInput.files[0] ? fileInput.files[0].name : '';
        const validExtensions = ['sql'];
        const fileExtension = fileName.split('.').pop().toLowerCase();

        if (!validExtensions.includes(fileExtension)) {
            e.preventDefault();
            Swal.fire({
                icon: 'error',
                title: 'Archivo inválido',
                text: 'Por favor, seleccione un archivo .sql antes de continuar.'
            });
            return;
        }

        const formData = new FormData(restoreForm);

        fetch(restoreUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                Swal.fire({
                    icon: 'success',
                    title: 'Éxito',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 1500
                }).then(() => {
                    location.reload();  // Recargar la página después del éxito
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: data.message
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al realizar la solicitud.'
            });
        });
    });
});