#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para 
# iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, 
# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o 
# computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual 
# número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido 
# pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram 
# necessários para vencer.
from random import randint
senha = '1234'
sen = input('DIgite a senha para começar: ').strip()
while sen != senha:
    print('Senha incorreta, tente novamente!')
    sen = input('Digite a senha para começar: ')
    if sen == senha:
        print()
        print('Se já errou na senha vai errar bastante no jogo kkkk')
print('-=' * 20)      
print('Seja bem vindo!')
print('Você está no jogo da adivinhação!')
print('Vou pensar em um número de 1 a 10 e você terá de adivinhá-lo!')
print('Boa sorte!')
print('-=' * 20)
num = str(randint(1,10))
qtent = 0
tentativa = 0
print(num)
while num != tentativa:
    qtent += 1 
    tentativa = str(input('Digite qual número eu pensei? ')).strip()
    while tentativa < num and tentativa != '10':
        print('Pensei em um número maior')
        tentativa = str(input('Digite qual número eu pensei? ')).strip()
        qtent += 1
    while tentativa > num or tentativa == '10':
        print('Pensei em um número menor')
        tentativa = str(input('Digite qual número eu pensei? ')).strip()
        qtent += 1
print('* * ' * 12)
print('PARABÉNS!! Você acertou!')
print(f'Você acertou na {qtent}ª tentativa.')    
