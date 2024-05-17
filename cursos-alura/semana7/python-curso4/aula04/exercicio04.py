# Colaboratory --> https://colab.research.google.com/notebooks/welcome.ipynb

# Aquecendo na programação
# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
# Coletamos os valores de início e fim
inicio = int(input('Insira o primeiro número inteiro: '))
fim = int(input('Insira o segundo número inteiro: '))

# Verificamos se o valor de início é maior que o fim
if inicio < fim:
  # podemos imprimir os inteiros entre o menor e o maior valor
  for i in range(inicio + 1, fim): 
    print(i)
elif inicio > fim:
  for i in range(fim + 1, inicio):
    print(i)
else: #caso os números sejam iguais, não conseguimos imprimir sequência alguma
  print('Os números são iguais.')

# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
# número inicial de bactérias
colonia_a = 4
colonia_b = 10

# taxas de crescimento das colônias
taxa_a = 0.03
taxa_b = 0.015

# contador de dias
dias = 0

# A condição que finaliza o laço é o caso em que
# a colônia A ultrapasse a colônia B
while colonia_a <= colonia_b:
  # usamos um operador de atribuição com multiplicação
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  # contamos o dia para cada iteração
  dias += 1

# resultado final
print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')

# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
# laço para pegar as 15 notas
for i in range(15):
  nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

  # verifica se a nota está entre 0 e 5
  # se estiver, o laço rodará ininterruptamente até ser obtido um valor válido
  while (nota < 0) or (nota > 5):
    nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

print('Verificação feita. Todas as notas são válidas')

# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
# coletamos a temperatura
temperatura = float(input('Insira a temperatura em Celsius: '))

# inicializamos uma contadora e soma para a média
contadora = 0
soma = 0

# nosso código executa sempre até o valor de temperatura for igual a -273
while temperatura != -273:
    # a soma é dada com a adição da temperatura à variavel soma
    soma += temperatura
    # contamos a quantidade de valores coletados através da contadora
    contadora += 1
    # coletamos novamente a temperatura
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A média das temperaturas é: {media}')

# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
# Pedir o número
num = int(input('Informe um número inteiro: '))

# Inicializar o cálculo
fatorial = 1

# nosso contador inicializa com o número máximo
# e será feita uma contagem decrescente com o operador -=
i = num
while i > 0:
    # queremos multiplicar agora o valor do fatorial pelo num
    # e todos os números abaixo dele até 1
    fatorial *= i
    i -= 1

# Imprimir o cálculo do fatorial
print(f'Fatorial de {num} é {fatorial}')

# Momento dos projetos
# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20

# Pedir o número
num = int(input('Informe um número inteiro de 1 a 10: '))

# Vamos gerar a tabuada
print(f'Tabuada do {num}:')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Solicitamos o número
num = int(input("Digite o número: "))

# Assumimos que o número é primo até que se prove o contrário
eh_primo = True

# Loop para verificar se o número é divisível por algum outro número
# Começa de 2, porque 1 não é um número primo, e vai até um número antes do próprio número
for i in range(2, num):
    # Se o número for divisível por qualquer número dentro deste intervalo,
    # ele não é primo, portanto, mudamos a variável 'eh_primo' para False e saímos do loop.
    if num % i == 0:
        eh_primo = False
        break

# Verifica se 'eh_primo' ainda é True, o que significa que o número passou pelo loop
# sem ser divisível por nenhum número além de 1 e ele mesmo.
if eh_primo == True:
    # Se for o caso, o número é primo.
    print(f'O número {num} é primo')
else:
    # Caso contrário, o número não é primo.
    print(f'O número {num} não é primo')

# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
# Coletamos as idades dos clientes
idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Inicializamos as variáveis de contadores
contador_0_25 = 0 # contador de idades entre 0 e 25
contador_26_50 = 0 # contador de idades entre 26 e 50
contador_51_75 = 0 # contador de idades entre 51 e 75
contador_76_100 = 0 # contador de idades entre 76 e 100

# nosso código executa sempre até o valor de idade for negativa
while idade >= 0:
    # contamos cada caso
    if idade >= 0 and idade <= 25:
        contador_0_25 += 1
    elif idade >= 26 and idade <= 50:
        contador_26_50 += 1
    elif idade >= 51 and idade <= 75:
        contador_51_75 += 1
    elif idade >= 76 and idade <= 100:
        contador_76_100 += 1
    
    # Repetir o processo de entrada de dados até que seja digitado um número negativo    
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Mostramos os resultados
print('Distribuição de idades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)

# 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
# Inicializamos as variáveis contadoras

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_branco = 0

# Início do laço para ler os votos
for i in range(0,20):
    voto = int(input('Informe seu voto: '))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Voto inválido.")

print(f'Votos candidato 1: {votos_candidato1}')
print(f'Votos candidato 2: {votos_candidato2}')
print(f'Votos candidato 3: {votos_candidato3}')
print(f'Votos candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos em branco: {votos_branco}')
print(f'Percentual de votos nulos: {(votos_nulos / 20 * 100)}')
print(f'Percentual de votos em branco: {(votos_branco / 20 * 100)}')

