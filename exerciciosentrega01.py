#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   # resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
mult = n1 * n2
divInt = n1 // n2
print(f'A soma dos dois valores é:{soma}')
print(f'A multiplicação entre os valores é: {mult}')
print(f'A divisão inteira deles é: {divInt}')
if n1 > n2:
    print(f'O maior dos dois números é:{n1}')
else:
    print(f'O maior dos dois números é:{n2}')
if soma % 2 == 0:
    print('O resultado da soma dos números é um número par')
else:
    print('O resultado da soma dos números é um número impar')
if divInt == 0:
    print('O resultado é ZERO(um número não pode ser dividido por zero)')
elif mult > 40:
    print(f'A multiplicação dos dois números dividido pelo resultado da sua divisão inteira é {mult / divInt}')
else:
    print('A multiplicação foi menor que 40')
