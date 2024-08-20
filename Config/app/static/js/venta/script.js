
    $(document).ready(function() {
        let itemCount = 0;

        function updateTotals() {
            let subtotal = 0;
            let totalIva = 0;
            const rows = $("#invoice-items tr");

            rows.each(function() {
                const cantidad = parseFloat($(this).find(".cantidad").val());
                const precioUnitario = parseFloat($(this).find(".precio-unitario").val());
                const iva = parseFloat($(this).find(".iva").val()) / 100;
                const totalSinIva = cantidad * precioUnitario;
                const totalConIva = totalSinIva * (1 + iva);
                $(this).find(".total").text(totalConIva.toFixed(1));
                subtotal += totalSinIva;
                totalIva += totalSinIva * iva;
            });

            $("#subtotal").text(subtotal.toFixed(1));
            const descuento = parseFloat($("#descuento").val()) / 100;
            const subtotalDto = subtotal * (1 - descuento);
            $("#subtotal_dto").text(subtotalDto.toFixed(1));
            $("#total_iva").text(totalIva.toFixed(1));
            const total = subtotalDto + totalIva;
            $("#total").text(total.toFixed(1));
        }

        function updateItemNumbers() {
            const rows = $("#invoice-items tr");
            rows.each(function(index) {
                $(this).find("td:first-child").text(index + 1);
            });
        }

        function updateProductData(selectElement) {
            const productoId = $(selectElement).val();
            if (productoId) {
                $.ajax({
                    url: '{% url "app:obtener_datos_producto" %}',
                    data: {
                        'producto_id': productoId
                    },
                    success: function(data) {
                        $(selectElement).closest('tr').find(".precio-unitario").val(data.precio);
                        updateTotals();
                    },
                    error: function() {
                        alert('Error al obtener los datos del producto.');
                    }
                });
            }
        }

        $("#add-item").on("click", function() {
            itemCount++;
            const row = `
                <tr>
                    <td>${itemCount}</td>
                    <td>
                        <select class="form-control producto_select" name="producto">
                            <option value="" hidden>Seleccione un producto</option>
                            {% for producto in productos %}
                                <option value="{{ producto.id }}">{{ producto.nombre }}</option>
                            {% endfor %}
                        </select>
                    </td>
                    <td><input type="number" class="cantidad" value="1" min="1" step="1" required></td>
                    <td><input type="number" class="precio-unitario" value="0" min="0" step="1" required></td>
                    <td><input type="number" class="iva" value="19" min="0" max="100" step="1" required></td>
                    <td class="total">0.0</td>
                    <td><button type="button" class="delete-item">Eliminar</button></td>
                </tr>
            `;
            $("#invoice-items").append(row);
            updateTotals();

            // Evento de cambio para el select de productos en la nueva fila
            $("#invoice-items").on("change", ".producto_select", function() {
                updateProductData(this);
            });

            $("#invoice-items").on("click", ".delete-item", function() {
                $(this).closest('tr').remove();
                itemCount--;
                updateItemNumbers();
                updateTotals();
            });
        });

        $("#invoice-items").on("input", ".cantidad, .precio-unitario, .iva", updateTotals);

        $("#print-invoice").on("click", function() {
            const accionesColumnas = $('th:last-child, td:last-child');
            accionesColumnas.hide();
            window.print();
            accionesColumnas.show();
        });
    });
