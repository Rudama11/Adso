$(document).ready(function() {
    // Inicializar Select2
    $('.select2').select2();

    // Evento al seleccionar un cliente
    $('#id_cliente').change(function() {
        var clienteId = $(this).val();
        if (clienteId) {
            $.ajax({
                url: '/path-to-your-api/cliente/' + clienteId + '/',  // Ajusta la URL de tu API
                type: 'GET',
                success: function(data) {
                    $('#id_numero_documento').val(data.numero_documento);
                    $('#id_nombre_cliente').val(data.nombre);
                    $('#id_direccion_cliente').val(data.direccion);
                    $('#id_correo_cliente').val(data.correo);
                    $('#id_telefono_cliente').val(data.telefono);
                }
            });
        }
    });

    // Evento al seleccionar un producto
    $('#id_producto').change(function() {
        var productoId = $(this).val();
        if (productoId) {
            $.ajax({
                url: '/path-to-your-api/producto/' + productoId + '/',  // Ajusta la URL de tu API
                type: 'GET',
                success: function(data) {
                    $('#id_precio_unitario').val(data.precio);
                }
            });
        }
    });
});