/* 3. Crie um array vazio chamado meuArray e adicione 3 números inteiros de sua escolha utilizando 
o método push(). Imprima no console os itens presentes no array para verificar se os números foram 
adicionados. Em seguida, substitua o primeiro elemento do array (índice 0) pelo dobro do seu valor atual. 
Imprima no console o array atualizado para verificar a mudança. */

const meuArray = []; // Criando um array vazio
meuArray.push(5); // Adicionando números ao array
meuArray.push(10);
meuArray.push(15);

//Exibição dos Itens
console.log("Itens no array meuArray:", meuArray);

//Atualização de Itens
//Dobrando o valor do primeiro elemento
meuArray[0] = meuArray[0] * 2; 
//mesma operação utilizando o operador `*=`
//meuArray[0] *= 2;
console.log("Array após a atualização do primeiro elemento:", meuArray);