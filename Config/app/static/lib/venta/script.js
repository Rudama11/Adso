document.addEventListener('DOMContentLoaded', function () {
    const productRows = document.getElementById('product-rows');

    function addProductRow() {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td><input type="number" class="product-id" min="0" required></td>
            <td><input type="number" class="product-quantity" min="1" required></td>
            <td><input type="text" class="product-detail" required></td>
            <td><input type="number" class="product-price" min="0" step="0.01" required></td>
            <td><input type="number" class="product-tax" min="0" max="100" step="0.01" required></td>
            <td><span class="product-total">$0.00</span></td>
            <td><button type="button" class="delete-row" onclick="deleteRow(this)">Eliminar</button></td>
        `;

        productRows.appendChild(row);

        // Revalidate the new row
        row.querySelectorAll('input').forEach(input => {
            input.addEventListener('input', validateInputs);
        });

        // Add delete functionality
        row.querySelector('.delete-row').addEventListener('click', function () {
            row.remove();
            validateInputs();
        });
    }

    function deleteRow(button) {
        const row = button.closest('tr');
        row.remove();
        validateInputs();
    }

    function validateInputs() {
        let isValid = true;
        let ids = new Set();
        let subtotal = 0;
        let taxes = 0;

        // Validate product rows
        document.querySelectorAll('#product-rows tr').forEach(row => {
            const id = row.querySelector('.product-id').value;
            const quantity = row.querySelector('.product-quantity').value;
            const price = row.querySelector('.product-price').value;
            const tax = row.querySelector('.product-tax').value;

            // Check for duplicate IDs
            if (ids.has(id)) {
                row.querySelector('.product-id').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-id').classList.remove('error');
                ids.add(id);
            }

            // Check for negative values
            if (quantity <= 0) {
                row.querySelector('.product-quantity').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-quantity').classList.remove('error');
            }

            if (price < 0) {
                row.querySelector('.product-price').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-price').classList.remove('error');
            }

            if (tax < 0 || tax > 100) {
                row.querySelector('.product-tax').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-tax').classList.remove('error');
            }

            // Calculate total price
            const total = (quantity * price * (1 + tax / 100)).toFixed(2);
            row.querySelector('.product-total').textContent = `$${total}`;

            // Accumulate totals
            subtotal += parseFloat(price * quantity); // Sumar al subtotal
            taxes += parseFloat(total) - parseFloat(price * quantity); // Sumar a los impuestos
        });

        // Calculate final values
        const total = (subtotal + taxes).toFixed(2); // Total final

        // Update totals in the HTML
        document.getElementById('subtotal').textContent = `$${subtotal.toFixed(2)}`; // Mostrar subtotal
        document.getElementById('taxes').textContent = `$${taxes.toFixed(2)}`; // Mostrar impuestos
        document.getElementById('total').textContent = `$${total}`; // Mostrar total

        // Validate company and client details
        const requiredFields = document.querySelectorAll('#company-name, #company-address, #company-nit, #company-email, #company-phone, #client-name, #client-address, #client-id, #client-email, #client-phone');

        requiredFields.forEach(field => {
            if (!field.checkValidity()) {
                field.classList.add('error');
                isValid = false;
            } else {
                field.classList.remove('error');
            }
        });

        return isValid;
    }

    function printInvoice() {
        if (validateInputs()) {
            window.print();
        } else {
            alert('Por favor, corrija los errores antes de imprimir la factura.');
        }
    }

    // Add event listener for inputs to validate dynamically
    document.querySelectorAll('input').forEach(input => {
        input.addEventListener('input', validateInputs);
    });

    window.addProductRow = addProductRow;
    window.printInvoice = printInvoice;
});
