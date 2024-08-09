
$(document).ready(function() {
    // Inicializar select2
    $('.select2').select2();

    // Evento para cuando cambie el cliente seleccionado
    $('#id_cliente').change(function() {
        var clienteID = $(this).val();
        if (clienteID) {
            $.ajax({
                url: '/api/clientes/' + clienteID + '/',
                type: "GET",
                dataType: "json",
                success: function(data) {
                    // Llenar los campos de correo, dirección y teléfono con los datos del cliente
                    $('#id_direccion').val(data.direccion);
                    $('#id_correo').val(data.correo);
                    $('#id_telefono').val(data.telefono);
                }
            });
        } else {
            $('#id_direccion').val('');
            $('#id_correo').val('');
            $('#id_telefono').val('');
        }
    });

    // Evento para cuando cambie el producto seleccionado
    $('#id_producto').change(function() {
        var productoID = $(this).val();
        if (productoID) {
            $.ajax({
                url: '/api/productos/' + productoID + '/',
                type: "GET",
                dataType: "json",
                success: function(data) {
                    // Llenar el campo de precio unitario con los datos del producto
                    $('#id_precio_unitario').val(data.precio);
                }
            });
        } else {
            $('#id_precio_unitario').val('');
        }
    });
});
