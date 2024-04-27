/* 4. Você recebeu dois arrays de nomes contendo os alunos da Turma A e da Turma B. */

const nomesTurmaA = [
    'João Silva',
    'Maria Santos',
    'Pedro Almeida'
  ];
  
  const nomesTurmaB = [
    'Carlos Oliveira',
    'Ana Souza',
    'Lucas Fernandes'
  ];

  /* Utilize o método concat() para unir os arrays das turmas A e B em um único array chamado todasAsTurmas.
   Depois, utilize o método find() para buscar um aluno específico pelo nome no array todosAlunos. 
   Exiba no console uma mensagem informando o nome do aluno procurado; caso não exista na lista, retorne
    uma mensagem de aviso, por exemplo Aluno não encontrado. */

const todosAlunos = nomesTurmaA.concat(nomesTurmaB);
const alunoProcurado = todosAlunos.find(nome => nome === 'Ana Souza');

if (alunoProcurado) {
  console.log('Aluno encontrado:', alunoProcurado);
} else {
  console.log('Aluno não encontrado.');
}