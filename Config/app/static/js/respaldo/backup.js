// Mostrar nombre del archivo seleccionado y manejar la visibilidad del input
document.getElementById('select-file-button').addEventListener('click', function() {
    document.getElementById('backup-file-input').click();
});

document.getElementById('backup-file-input').addEventListener('change', function() {
    var fileName = this.files[0] ? this.files[0].name : 'Sin archivos seleccionados';
    document.getElementById('file-name').textContent = fileName;
});

// Validación de selección de archivo
document.getElementById('restore-form').addEventListener('submit', function(event) {
    var fileInput = document.getElementById('backup-file-input');
    if (!fileInput.files.length) {
        event.preventDefault(); // Prevenir el envío del formulario
        Swal.fire({
            icon: 'warning',
            title: 'Advertencia',
            text: 'Debe seleccionar un archivo para restaurar el backup.',
        });
    }
});