function calculate(operator) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const resultDiv = document.getElementById('result');

    if ((isNaN(num1) || num1 === '') || (operator !== '√' && (isNaN(num2) || num2 === ''))) {
        resultDiv.innerHTML = 'Por favor, ingresa números válidos';
        resultDiv.className = 'error';
        return;
    }

    const n1 = parseFloat(num1);
    const n2 = parseFloat(num2);
    let result;

    switch (operator) {
        case '+':
            result = n1 + n2;
            break;
        case '-':
            result = n1 - n2;
            break;
        case '*':
            result = n1 * n2;
            break;
        case '/':
            if (n2 === 0) {
                resultDiv.innerHTML = 'No se puede dividir por 0';
                resultDiv.className = 'error';
                return;
            }
            result = n1 / n2;
            break;
        case '^':
            result = Math.pow(n1, n2);
            break;
        case '√':
            if (n1 < 0) {
                resultDiv.innerHTML = 'No se puede calcular la raíz cuadrada de un número negativo';
                resultDiv.className = 'error';
                return;
            }
            result = Math.sqrt(n1);
            break;
        case 'C':
            document.getElementById('num1').value = '';
            document.getElementById('num2').value = '';
            resultDiv.innerHTML = '';
            return;
        default:
            resultDiv.innerHTML = 'Operación no válida';
            resultDiv.className = 'error';
            return;
    }

    resultDiv.innerHTML = `Resultado: ${n1} ${operator} ${n2} = ${result}`;
    resultDiv.className = '';
}

document.getElementById('num1').addEventListener('input', function() {
    const num2Input = document.getElementById('num2');
    const operator = document.querySelector('.buttons button:focus');
    if (operator && operator.innerHTML === '√') {
        num2Input.style.display = 'none';
    } else {
        num2Input.style.display = '';
    }
});