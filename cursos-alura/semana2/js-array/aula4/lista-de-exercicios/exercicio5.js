/* 5. Considere um array de números inteiros. */

const numeros = [6, 9, 12, 15, 18, 21];

/* Utilize o método forEach() para multiplicar cada elemento do array por 3 e exibir o resultado de 
cada multiplicação. Depois, utilize o método findIndex() para encontrar o índice do número 18 no array. */

const numeros = [6, 9, 12, 15, 18, 21];

console.log('Elementos do array multiplicados por 3:');

numeros.forEach(numero => {
  const resultado = numero * 3;
  console.log(resultado);
});

const indiceDoNumero18 = numeros.findIndex(numero => numero === 18);

if (indiceDoNumero18 !== -1) {
  console.log(`O número 18 está no índice ${indiceDoNumero18}.`);
} else {
  console.log('O número 18 não está presente no array.');
}