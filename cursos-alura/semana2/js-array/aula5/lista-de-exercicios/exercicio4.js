/* 4. Escreva uma função que receba um array de números e retorne um array contendo apenas os números pares. */

function filtraNumerosPares(arr) {
    return arr.filter(num => num % 2 === 0); // Filtra apenas os números pares
}

const numArray = [1, 2, 3, 4, 5, 6];
const listaNumerosPares = filtraNumerosPares(numArray);
console.log(listaNumerosPares); // Saída: [2, 4, 6]