#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
#venceu ou perdeu.

import random
from time import sleep
print('-' * 10, '\nVou pensar em um número entre 0 a 5, tente adivinhar.')
num = random.randint(0, 5)
num_u = int(input('Digite um número entre 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
print('-' * 10)
if num_u == num:
    print('O número escolhido pela máquina foi {}, seu número foi {}. Parabéns! Você acertou =)'.format(num, num_u))
else:
    print('O número escolhido pela máquina foi {}, seu número foi {}. Que pena! Você errou! =('.format(num, num_u))

