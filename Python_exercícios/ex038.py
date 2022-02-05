#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

print('Vamos descobrir qual o maior e menor valor entre dois números:')
print('-' * 10)
print('...ANALISADOR DE NÚMEROS...')
print('-' * 10)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('{} é o maior número e {} é o menor.'.format(num1, num2))
elif num1 < num2:
    print('{} é o maior número e {} é o menor.'.format(num2, num1))
else:
    print('Os números são iguais.')


