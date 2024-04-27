/* 2. Crie uma função chamada executaOperacaoEmArray que recebe dois parâmetros: um array e uma função 
de callback que executa alguma operação matemática. Essa função deve iterar por cada elemento do array 
e aplicar a função de callback em cada um dos elementos, imprimindo o resultado da operação no console. */

function executaOperacaoEmArray(array, funcaoCallback) {
    return array.map(funcaoCallback); // Executa a função de callback em cada elemento do array
}

function dobraNumero(num) {
    return num * 2; // Função de exemplo para dobrar o número
}

const listaNumeros = [1, 2, 3];
const listaNumerosDobrados = executaOperacaoEmArray(listaNumeros, dobraNumero);
console.log(listaNumerosDobrados); // Saída: [2, 4, 6]