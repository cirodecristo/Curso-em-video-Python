# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci. Exemplo:
#
# 0 – 1 – 1 – 2 – 3 – 5 – 8
import sys

print('-' * 10)
print('DEQUÊNCIA DE FIBONACCI')
print('-' * 10)
term = int(input('Quandos termos você quer mostrar? '))
print('~' * 10)
c = 1
n1 = 0
n2 = 1
n3 = 0

while c < term - 1:
    n3 = n1 + n2
    if n1 == 0:
        print('{} -> {} -> '.format(n1, n2), end='')
    print('{} -> '.format(n3), end='')
    if c == term:
        print('{}'.format(n3))
    n1 = n2
    n2 = n3
    c += 1

print('FIM')
print('~' * 10)
