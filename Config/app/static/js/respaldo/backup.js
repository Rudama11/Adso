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

    // Actualizar el nombre del archivo seleccionado
    fileInput.addEventListener('change', function() {
        const fileName = fileInput.files[0] ? fileInput.files[0].name : 'Sin archivos seleccionados';
        fileNameDisplay.textContent = fileName;
    });

    // Manejar el envío del formulario de backup
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

    // Manejar el envío del formulario de restauración
    restoreForm.addEventListener('submit', function(e) {
        e.preventDefault();
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