# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# import random
# from time import sleep
# print('-' * 10, '\nVou pensar em um número entre 0 a 10, tente adivinhar.')
# num = random.randint(0, 10)
# num_u = int(input('Digite um número de 0 a 10: '))
# tent = 0
# print('PROCESSANDO...')
# sleep(1)
# print('-' * 10)
# while num_u > 10:
#     num_u = int(input('Opção inválida: Digite um número de 0 e 10: '))
# while num_u != num:
#     if num_u > num:
#         print('Que pena! Você errou, digite um número MENOR')
#     if num_u < num:
#         print('Que pena! Você errou, digite um número MAIOR')
#     tent += 1
#     num_u = int(input('Digite um número entre 0 a 10: '))
#
# print('O número escolhido pela máquina foi {}, seu número foi {}. Parabéns! Você acertou =)\nforam necessárias {} '
#       'tentativas para acertar'.format(num, num_u, tent))

from random import randint
num_cpu = randint(0, 10)
print('Olá, sou o computador!\nEscolhi um número entre 0 e 10, consegue adivinhar:')
acertou = False
tent = 0
while not acertou:
    jogador = int(input('Digite um número: '))
    tent += 1
    if jogador > num_cpu:
        print('Errou! Digite um número MENOR')
    elif jogador < num_cpu:
        print('Errou! Digite um número MAIOR')
    else:
        print('Acertou! Eu digitei {} e você também. Foram necessárias {} tentativas'.format(num_cpu, tent))
        acertou = True





