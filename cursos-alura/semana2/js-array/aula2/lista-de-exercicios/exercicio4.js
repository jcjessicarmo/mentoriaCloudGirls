/* 4. Crie dois arrays chamados menuPrincipal e menuDeSobremesas contendo opções do cardápio 
de um restaurante. Utilize o método concat para criar um novo array menuCompleto contendo todos os 
elementos de menuPrincipal seguidos pelos elementos de menuDeSobremesas. */

const menuPrincipal = ['lasanha', 'feijoada', 'macarronada'];
const menuDeSobremesas = ['pudim', 'sorvete', 'brigadeiro'];
const menuCompleto = menuPrincipal .concat(menuDeSobremesas);
console.log('Veja o menu completo:', menuCompleto );