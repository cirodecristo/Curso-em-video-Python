# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

import sys
from time import sleep
n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
opc = 0

while opc != 5:
    print('-----MENU DE OPÇÕES-----')
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    opc = int(input('Escolha uma das opções acima para prosseguir: '))
    if opc == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opc == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            print('{} é o maior número'.format(n1))
        else:
            print('{} é o maior número'.format(n2))
    elif opc == 4:
        print('Informe os números novamente')
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
        print('Informe os números novamente')
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
sleep(1)
print('Fim do programa')





