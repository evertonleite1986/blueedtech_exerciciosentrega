#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma 
# string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e 
# mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = str(input('Digite uma frase: ')).lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for c in frase:
    if c == 'a':
        a += 1
    if c == 'e':
        e += 1
    if c == 'i':
        i += 1
    if c == 'o':
        o += 1
    if c == 'u':
        u += 1             
print(f'A quantidade de letras A digitadas é: {a}')
print(f'A quantidade de letras E digitadas é: {e}')
print(f'A quantidade de letras I digitadas é: {i}')
print(f'A quantidade de letras O digitadas é: {o}')
print(f'A quantidade de letras U digitadas é: {u}')
for c in "aeiou":
    frase = frase.replace(c, " ")
print(f'{frase}')
