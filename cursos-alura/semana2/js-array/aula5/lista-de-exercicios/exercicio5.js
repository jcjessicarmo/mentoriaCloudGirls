/* 5. Crie uma função que filtre os números de um array que são múltiplos de 3 e maiores que 5. */

const listaNumeros = [3, 6, 9, 4, 12, 2, 7];

function filtraNumeros(arr) {
    return arr.filter(num => num % 3 === 0 && num > 5); // Filtra números múltiplos de 3 e maiores que 5
}

const numerosFiltrados = filtraNumeros(listaNumeros);
console.log(numerosFiltrados); // Saída: [6, 9, 12]