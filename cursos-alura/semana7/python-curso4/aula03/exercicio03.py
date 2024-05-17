# Colaboratory --> https://colab.research.google.com/notebooks/welcome.ipynb

# Aquecendo na programação
# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
# Coletar os números
num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))

# Comparamos ambos os números e descobrimos qual é o maior
if num1 > num2:
    print(f'O primeiro número é maior: {num1}')
elif num2 > num1:
    print(f'O segundo número é maior: {num2}')
else: # Caso os números sejam iguais
    print('Os dois números são iguais.')

# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
# Coleta do percentual
variacao = float(input('Digite o percentual de crescimento: '))

# Verifica se o valor é positivo ou negativo com uma verificação se o número
# é maior ou menor que 0
if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve um decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento.')

# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
# Coletamos a letra da pessoa usuária como minúscula
letra = input('Digite uma letra: ').lower()
vogais = 'aeiou' # string contendo todos os dados

# Verificamos se a letra está nas vogais com in
if letra in vogais:
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')

# 4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
# Coletamos os preços dos 3 anos
preco_ano1 = float(input('Informe o preço médio do carro no primeiro ano: '))
preco_ano2 = float(input('Informe o preço médio do carro no segundo ano: '))
preco_ano3 = float(input('Informe o preço médio do carro no terceiro ano: '))

# Determinamos o maior valor através de comparações
maior = preco_ano1
if preco_ano2 > maior:
  maior = preco_ano2
if preco_ano3 > maior:
  maior = preco_ano3

# Determinamos o menor valor através de comparações
menor = preco_ano1
if preco_ano2 < menor:
  menor = preco_ano2
if preco_ano3 < menor:
  menor = preco_ano3

# Mostramos o resultado
print(f'O preço mais alto foi de R$ {maior}.')
print(f'O preço mais baixo foi de R$ {menor}.')

# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
# Coletamos os preços dos três produtos
p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

# Verificamos qual produto é o mais barato usando o operador lógico 'and'
if p1 < p2 and p1 < p3:
    print('O primeiro produto é o mais barato.')
elif p2 < p1 and p2 < p3:
    print('O segundo produto é o mais barato.')
elif p3 < p1 and p3 < p2:
    print('O terceiro produto é o mais barato.')
elif p1 == p2 == p3:
    print('Os produtos possuem o mesmo preço.')
else:
    # Identificamos quais produtos possuem o mesmo preço, se for o caso
    if p1 == p2:
        print('O primeiro e o segundo produtos são os mais baratos.')
    elif p2 == p3:
        print('O segundo e terceiro produtos são os mais baratos.')
    elif p1 == p3:
        print('O primeiro e o terceiro produtos são os mais baratos.')

# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.
# Coletamos os 3 números
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

# Comparação entre os 3 números
if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
# Coletamos o turno de estudo
turno = input('Digite em qual turno você estuda (manhã, tarde ou noite): ')

# Comparamos a entrada com todas as opções e imprimimos o resultado.
if turno == 'manhã':
  print('Bom Dia!')
elif turno == 'tarde':
  print('Boa Tarde!')
elif turno == 'noite':
  print('Boa Noite!')
else:
  print('Valor Inválido!')

# 8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
# Coletamos os dados
num = int(input('Digite um número: '))

# Verificamos se o número é par através do resultado do módulo
if num % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

# 9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
# Coletamos os dados
num = float(input('Digite um número: '))

# Verificamos se o número é inteiro ou decimal através do resultado do módulo
if num % 1 == 0:
    print('O número é inteiro.')
else:
    print('O número é decimal.')

# Momento dos projetos
# 10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
# Coletamos os números a serem operados e solicitamos a operação desejada pela pessoa usuária
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
operacao = input('Informe a operação desejada (+, -, *, /): ')

# Verificamos o operador que foi selecionado e executa a operação matemática conforme a seleção
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else: # Especificamos um resultado caso a pessoa usuária não digite alguma das operações corretamente.
    print('Operação inválida, resultado da operação será 0')
    resultado = 0 

#  Fazemos as mesmas verificações das questões anteriores para fazer o relatório do cálculo entre números
if resultado % 1 == 0:
    print('O resultado é inteiro.')
else:
    print('O resultado é decimal.')

if resultado > 0:
    print('O resultado é positivo.')
elif resultado == 0:
    print('O resultado é neutro.')
else:
    print('O resultado é negativo.')

if resultado % 2 == 0:
    print('O resultado é par.')
else:
    print('O resultado é ímpar.')

# 11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

# Coletamos os lados de um triângulo
print('Coletaremos os lados de um triângulo.')
lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

# Verificamos de os lados formam um triângulo
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('Os valores podem formar um triângulo!')
    # comparamos os lados para verificar o tipo de triângulo
    if (lado1 == lado2) and (lado2 == lado3):
        print('O triângulo é equilátero.')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isósceles.')
else:
    print('Os valores não podem formar um triângulo!')

# 12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
# Coletamos a quantidade de litros e o tipo de combustível,
# já deixando o caractere em maiúsculo para facilitar nossa análise
quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = input('Informe o tipo de combustível (E para etanol e D para diesel): ').upper()

#  Verificamos primeiro o tipo de combustível
if tipo_combustivel == 'E':
  # Taxamos o valor do preço em litros do etanol
  preco_litro = 1.70
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
elif tipo_combustivel == 'D':
  # Taxamos o valor do preço em litros do disel
  preco_litro = 2.00
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05
# Caso ocorra um erro na especificação de tipo de combustível,
# consideramos entradas inválidas, e os preços são taxados em 0
else:
    print('Entradas inválidas!')
    preco_litro = 0
    desconto = 0

# Fazemos o cálculo do valor de desconto, seguido do cálculo do preço descontado
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

# Resultado
print(f'Valor a ser pago pelo cliente: R$ {valor_pago}')

# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.

# Coletamos as vendas dos dois anos
venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

# Calculamos a variação percentual entre as vendas dos anos de 2022 e 2023
var_percentual = 100 * (venda_2023 - venda_2022) / (venda_2022)

# Análise condicional da variação percentual para determinar a sugestão a ser enviada
if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')
