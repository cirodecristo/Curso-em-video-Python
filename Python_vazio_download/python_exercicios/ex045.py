#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('VAMOS JOGAR JOKENPÔ')
print('✌🖐✊' * 10)
num_com = randint(1, 3)
num_usu = int(input('*Para escolher "PAPEL" digite: 1\n*Par escolher "PEDRA" digite: 2\n*Para escolher "TESOURA"'
                    ' digite: 3\n\nEscolha um número: '))
sleep(0.5)
print('{:=^40}'.format('JO'))
sleep(0.5)
print('{:=^40}'.format('KEN'))
sleep(0.5)
print('{:=^40}'.format('PÔ'))
sleep(0.5)

if num_usu == num_com:
    if num_usu == 1:
        num_usu = '🖐'
    elif num_usu == 2:
        num_usu = '✊'
    elif num_usu == 3:
        num_usu = '✌'
    num_com = num_usu
    print('Empate! Você tirou {} e a máquina tirou {}'.format(num_usu, num_com))
elif (num_usu == 1 and num_com == 2) or (num_usu == 2 and num_com == 3) or (num_usu == 3 and num_com == 1):
    if num_usu == 1:
        num_usu = '🖐'
    elif num_usu == 2:
        num_usu = '✊'
    elif num_usu == 3:
        num_usu = '✌'
    if num_com == 1:
        num_com = '🖐'
    elif num_com == 2:
        num_com = '✊'
    elif num_com == 3:
        num_com = '✌'
    print('VENCEU! Você escolheu {} e a máquina escolheu {}'.format(num_usu, num_com))
elif (num_usu == 1 and num_com == 3) or (num_usu == 2 and num_com == 1) or (num_usu == 3 and num_com == 2):
    if num_usu == 1:
        num_usu = '🖐'
    elif num_usu == 2:
        num_usu = '✊'
    elif num_usu == 3:
        num_usu = '✌'
    if num_com == 1:
        num_com = '🖐'
    elif num_com == 2:
        num_com = '✊'
    elif num_com == 3:
        num_com = '✌'
    print('PERDEU! Você tirou {} e a máquina tirou {}'.format(num_usu, num_com))

