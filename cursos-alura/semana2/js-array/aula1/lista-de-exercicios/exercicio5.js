/* 5. Desenvolva um programa em Node.js que simule uma clínica veterinária. 
Crie um array vazio chamado clinica que representará a fila de animais na clínica. 
Em um primeiro momento, simule a chegada de três animais diferentes e exiba a lista de animais no console.
Após a exibição, remova os animais da lista um por vez e, por fim, exiba no console o estado final da lista. */

// Criando um array vazio para representar a fila de animais na clínica
const clinica = [];

// Chegada de animais na clínica
clinica.push("Cachorro");
clinica.push("Gato");
clinica.push("Coelho");

// Exibindo a fila de animais na clínica após a chegada
console.log("Fila de animais após a chegada: ", clinica);

// Removendo cada animal da lista:
clinica.pop();
clinica.pop();
clinica.pop();

// Exibindo o estado final da lista:
console.log("Fila de animais aguardando: ", clinica);