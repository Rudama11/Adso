$(document).ready(function() {
    // Inicializa select2 en los campos correspondientes
    $('#id_cliente').select2({
        ajax: {
            url: '/path-to-your-api/cliente/',  // URL de la API para clientes
            dataType: 'json',
            delay: 250,
            processResults: function(data) {
                return {
                    results: $.map(data, function(item) {
                        return {
                            id: item.id,
                            text: item.numero_documento + ' - ' + item.nombre
                        };
                    })
                };
            },
            cache: true
        },
        placeholder: 'Seleccione un cliente',
        minimumInputLength: 1,
        templateResult: function(data) {
            if (!data.id) {
                return data.text;
            }
            return $('<span>' + data.text + '</span>');
        }
    });

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

    $('#id_producto').select2({
        ajax: {
            url: '/path-to-your-api/producto/',  // URL de la API para productos
            dataType: 'json',
            delay: 250,
            processResults: function(data) {
                return {
                    results: $.map(data, function(item) {
                        return {
                            id: item.id,
                            text: item.descripcion
                        };
                    })
                };
            },
            cache: true
        },
        placeholder: 'Seleccione un producto',
        minimumInputLength: 1
    });

    $('#id_producto').change(function() {
        var productoId = $(this).val();
        if (productoId) {
            $.ajax({
                url: '/path-to-your-api/producto/' + productoId + '/',
                type: 'GET',
                success: function(data) {
                    $('#id_precio_unitario').val(data.precio);
                }
            });
        }
    });
});
