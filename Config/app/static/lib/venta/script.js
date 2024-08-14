document.addEventListener("DOMContentLoaded", () => {
    const addItemButton = document.getElementById("add-item");
    const invoiceItems = document.getElementById("invoice-items");
    let itemCount = 0; // Contador para el número de ítem
    
    addItemButton.addEventListener("click", () => {
        itemCount++; // Incrementar el contador cada vez que se agrega un nuevo ítem
        const row = document.createElement("tr");
        
        row.innerHTML = `
            <td>${itemCount}</td> <!-- Mostrar el número de ítem -->
            <td><input type="text" class="descripcion" required></td>
            <td><input type="number" class="cantidad" value="1" min="1" required></td>
            <td><input type="number" class="precio-unitario" value="0" min="0" step="0.01" required></td>
            <td class="total">0,00</td>
            <td><button type="button" class="delete-item">Eliminar</button></td>
        `;
        
        invoiceItems.appendChild(row);
        updateTotals();

        row.querySelector(".delete-item").addEventListener("click", () => {
            invoiceItems.removeChild(row);
            itemCount--; // Decrementar el contador al eliminar un ítem
            updateItemNumbers(); // Actualizar los números de ítem
            updateTotals();
        });
    });
    
    invoiceItems.addEventListener("input", updateTotals);

    function updateTotals() {
        let subtotal = 0;
        const rows = invoiceItems.querySelectorAll("tr");

        rows.forEach(row => {
            const cantidad = parseFloat(row.querySelector(".cantidad").value);
            const precioUnitario = parseFloat(row.querySelector(".precio-unitario").value);
            const total = cantidad * precioUnitario;
            row.querySelector(".total").textContent = total.toFixed(2);
            subtotal += total;
        });

        document.getElementById("subtotal").textContent = subtotal.toFixed(2);

        const descuento = parseFloat(document.getElementById("descuento").value);
        const subtotalDto = subtotal - descuento;
        document.getElementById("subtotal_dto").textContent = subtotalDto.toFixed(2);

        const iva = parseFloat(document.getElementById("iva").value);
        const totalIva = subtotalDto * (iva / 100);
        document.getElementById("total_iva").textContent = totalIva.toFixed(2);

        const total = subtotalDto + totalIva;
        document.getElementById("total").textContent = total.toFixed(2);
    }

    function updateItemNumbers() {
        const rows = invoiceItems.querySelectorAll("tr");
        rows.forEach((row, index) => {
            row.querySelector("td:first-child").textContent = index + 1; // Actualiza el número de ítem
        });
    }

    // Agregar evento al botón de imprimir
    const printButton = document.getElementById("print-invoice"); // Asegúrate de que el ID coincida
    if (printButton) {
        printButton.addEventListener("click", () => {
            window.print(); // Llama a la función de impresión del navegador
        });
    } else {
        console.error("Botón de impresión no encontrado");
    }
});