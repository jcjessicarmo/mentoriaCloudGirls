# Colaboratory --> https://colab.research.google.com/notebooks/welcome.ipynb

# Coleta e amostragem de dados
# Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
# Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
# Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

# 1) Podemos solicitar o nome com a função input e atribuir o resultado da saída a uma variável. Na sequência, podemos imprimir o resultado da variável na função print usando a formatação f-string.
nome = input('Digite seu nome: ')
print(f'Olá, {nome}.')

# 2) Podemos solicitar o nome e a idade com a função input e atribuir o resultado da saída a uma variável. No caso da idade, é necessária uma conversão da saída do input para um valor inteiro com a função int(). Em seguida, podemos imprimir o resultado das coletas na função print usando a formatação f-string.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'Olá {nome}, você tem {idade} anos.')

# 3) Podemos solicitar o nome, a idade e a altura com a função input e atribuir o resultado da saída a uma variável. No caso da idade, é necessária uma conversão da saída do input para um valor inteiro com a função int(). Já para a altura, é preciso realizar uma conversão para o valor de tipo float com a função float(). Em seguida, podemos imprimir o resultado das coletas na função print usando a formatação f-string.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
print(f'Olá {nome}, você tem {idade} anos e mede {altura} metros!')


# Calculadora com operadores
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
# Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
# Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
# Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
# Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

# 1) Podemos coletar os dois valores com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da soma entre as duas entradas com +.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a+b)

# 2) Usando a mesma lógica da questão anterior, podemos coletar os três valores com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da soma entre as três entradas com +.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print(a+b+c)

# 3) Podemos coletar os dois valores com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da subtração entre as duas entradas com -.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a-b)

# 4) Podemos coletar os dois valores com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da multiplicação entre as duas entradas com *.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a*b)

# 5) Podemos coletar o numerador e denominador com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da divisão entre as duas entradas com /.
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador/denominador)

# 6) Podemos coletar o operador e potência com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da exponenciação com **.
operador = int(input('Digite o operador valor: '))
potencia = int(input('Digite a potência valor: '))
print(operador**potencia)

# 7) Podemos coletar o numerador e denominador com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado da divisão inteira entre as duas entradas com //.
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador//denominador)

# 8) Podemos coletar o numerador e denominador com input e converter a saída para um inteiro com a função int(). Com o print, é possível mostrar o resultado do resto da divisão entre as duas entradas com %.
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador%denominador)

# 9) Podemos coletar as três notas com input e converter a saída para um float com a função float(). Com o print e formatação f-string, é possível mostrar o resultado da média entre as três variáveis somando as notas com + e dividindo o valor da soma com /.
nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
print(f'Média {(nota_1+nota_2+nota_3)/3}.')

# 10) Calculamos a média ponderada multiplicando os pesos pelos seus respectivos valores e somando o resultado entre cada multiplicação. O valor dessas somas é dividido pela soma total dos pesos. Com o print, imprimimos o resultado do cálculo da média.
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Média {media_ponderada}.')


# Editando textos
# Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
# Crie um código que solicite uma frase e depois imprima a frase na tela.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
# Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.

# 1) Definimos uma frase qualquer entre aspas simples e imprimimos ela inserindo a variável dentro de um print.
frase = 'Olá Python!'
print(frase)

# 2) Coletamos uma frase a partir da função input e imprimimos o resultado com a função print.
frase = input('Digite uma frase: ')
print(frase)

# 3) Coletamos uma frase a partir da função input e conseguimos mostrar seu valor em maiúsculo com o método upper. Podemos mostrar a saída dele em uma função print.
frase = input('Digite uma frase: ')
print(frase.upper())

# 4) Coletamos uma frase a partir da função input e conseguimos mostrar seu valor em minúsculo com o método lower. Podemos mostrar a saída dele em uma função print.
frase = input('Digite uma frase: ')
print(frase.lower())

# 5) Para o exemplo, é interessante definir uma frase com espaços no início e no fim da frase. Definido isso, podemos remover esses espaços com o método strip e mostramos o resultado na função print.
frase = ' Olá Python!  '
print(frase.strip())

# 6) Coletamos uma frase a partir da função input, mesmo não sabendo se ela terá espaços no início e no fim da frase, e podemos remover esses espaços com o método strip. O resultado pode ser exposto na função print.
frase = input('Digite uma frase: ')
print(frase.strip())

# 7) Coletamos uma frase a partir da função input, mesmo não sabendo se ela terá espaços no início e no fim da frase; podemos remover esses espaços com o método strip e também utilizar o método lower agrupado ao método strip. O resultado pode ser exposto na função print.
frase = input('Digite uma frase: ')
print(frase.strip().lower())

# 8) Coletamos uma frase a partir da função input. Para ter certeza de que os caracteres não vão estar em letras maiúsculas, podemos deixar toda a frase em letras minúsculas com o método lower e depois agrupamos o resultado da função ao método replace, definindo o valor a ser substituído como 'e' e o novo valor como 'f'. O resultado é exposto na função print.
frase = input('Digite uma frase: ')
print(frase.lower().replace('e','f'))

# 9) Coletamos uma frase a partir da função input. Para ter certeza de que os caracteres não vão estar em letras maiúsculas, podemos deixar toda a frase em letras minúsculas com o método lower e depois agrupamos o resultado da função ao método replace, definindo o valor a ser substituido como 'a' e o novo valor como o caractere 64 pela tabela Unicode, que corresponde ao caractere @. O resultado é exposto na função print.
frase = input('Digite uma frase: ')
print(frase.lower().replace('a',chr(64)))

# 10) Coletamos uma frase a partir da função input. Para ter certeza de que os caracteres não vão estar em letras maiúsculas, podemos deixar toda a frase em letras minúsculas com o método lower e depois agrupamos o resultado da função ao método replace, definindo o valor a ser substituido como 's' e o novo valor como o caractere 36 pela tabela Unicode, que corresponde ao caractere $. O resultado é exposto na função print.
frase = input('Digite uma frase: ')
print(frase.lower().replace('s',chr(36)))