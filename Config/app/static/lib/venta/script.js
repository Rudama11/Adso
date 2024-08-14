document.addEventListener("DOMContentLoaded", () => {
    const addItemButton = document.getElementById("add-item");
    const invoiceItems = document.getElementById("invoice-items");
    let itemCount = 0;
    
    addItemButton.addEventListener("click", () => {
        itemCount++;
        const row = document.createElement("tr");
        
        row.innerHTML = `
            <td>${itemCount}</td> <!-- Mostrar el número de ítem -->
            <td><input type="text" class="descripcion" required></td>
            <td><input type="number" class="cantidad" value="1" min="1" step="1" required></td>
            <td><input type="number" class="precio-unitario" value="0" min="0" step="1" required></td>
            <td><input type="number" class="iva" value="19" min="0" max="100" step="1" required></td>
            <td class="total">0.0</td>
            <td><button type="button" class="delete-item">Eliminar</button></td>
        `;
        
        invoiceItems.appendChild(row);
        updateTotals();

        row.querySelector(".delete-item").addEventListener("click", () => {
            invoiceItems.removeChild(row);
            itemCount--;
            updateItemNumbers();
            updateTotals();
        });
    });
    
    invoiceItems.addEventListener("input", updateTotals);

    function updateTotals() {
        let subtotal = 0;
        let totalIva = 0;
        const rows = invoiceItems.querySelectorAll("tr");

        rows.forEach(row => {
            const cantidad = parseFloat(row.querySelector(".cantidad").value);
            const precioUnitario = parseFloat(row.querySelector(".precio-unitario").value);
            const iva = parseFloat(row.querySelector(".iva").value) / 100;
            const totalSinIva = cantidad * precioUnitario;
            const totalConIva = totalSinIva * (1 + iva);
            row.querySelector(".total").textContent = totalConIva.toFixed(1);
            subtotal += totalSinIva;
            totalIva += totalSinIva * iva;
        });

        document.getElementById("subtotal").textContent = subtotal.toFixed(1);

        const descuento = parseFloat(document.getElementById("descuento").value) / 100;
        const subtotalDto = subtotal * (1 - descuento);
        document.getElementById("subtotal_dto").textContent = subtotalDto.toFixed(1);

        document.getElementById("total_iva").textContent = totalIva.toFixed(1);

        const total = subtotalDto + totalIva;
        document.getElementById("total").textContent = total.toFixed(1);
    }

    function updateItemNumbers() {
        const rows = invoiceItems.querySelectorAll("tr");
        rows.forEach((row, index) => {
            row.querySelector("td:first-child").textContent = index + 1;
        });
    }

    const printButton = document.getElementById("print-invoice");
    if (printButton) {
        printButton.addEventListener("click", () => {
            const accionesColumnas = document.querySelectorAll('th:last-child, td:last-child');
            accionesColumnas.forEach(columna => {
                columna.style.display = 'none';
            });

            window.print();

            accionesColumnas.forEach(columna => {
                columna.style.display = '';
            });
        });
    } else {
        console.error("Botón de impresión no encontrado");
    }
});