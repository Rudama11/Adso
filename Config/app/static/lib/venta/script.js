$(document).ready(function() {
    $('.select2').select2();

    // Manejar el cambio en el selector de cliente
    $('#id_cliente').change(function() {
        var clienteId = $(this).val();
        
        // Realiza una llamada AJAX para obtener los datos del cliente
        $.ajax({
            url: '/ruta/al/api/clientes/' + clienteId, // Asegúrate de que esta URL es correcta
            method: 'GET',
            success: function(data) {
                $('#cliente-correo').text(data.correo);
                $('#cliente-direccion').text(data.direccion);
                $('#cliente-telefono').text(data.telefono);
            },
            error: function() {
                // Manejo de errores
                $('#cliente-correo').text('');
                $('#cliente-direccion').text('');
                $('#cliente-telefono').text('');
            }
        });
    });

    // Manejar el cambio en el selector de producto
    $('select[name="producto"]').change(function() {
        var productoId = $(this).val();
        
        // Realiza una llamada AJAX para obtener los datos del producto
        $.ajax({
            url: '/ruta/al/api/productos/' + productoId, // Asegúrate de que esta URL es correcta
            method: 'GET',
            success: function(data) {
                $('#producto-precio').text(data.precio);
            },
            error: function() {
                // Manejo de errores
                $('#producto-precio').text('');
            }
        });
    });
});