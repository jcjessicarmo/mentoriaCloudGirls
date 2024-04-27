/* 3. Considere duas listas de cores: const coresLista1 = ['Vermelho', 'Verde', 'Azul', 'Amarelo', 'Vermelho'] 
const coresLista2 = ['Laranja', 'Verde', 'Roxo', 'Azul'] Crie um programa que una essas duas listas, 
removendo cores duplicadas e exiba a lista final. */

const coresLista1 = ['Vermelho', 'Verde', 'Azul', 'Amarelo', 'Vermelho'];
const coresLista2 = ['Laranja', 'Verde', 'Roxo', 'Azul'];

const coresUnicas = [...new Set([...coresLista1, ...coresLista2])];
console.log('Cores sem repetir: ', coresUnicas);