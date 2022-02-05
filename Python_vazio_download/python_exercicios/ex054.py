# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from textwrap import wrap
from datetime import datetime
atual = datetime.today().year
cont_ma = 0
cont_me = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    idade = atual - ano
    if idade < 21:
        cont_me += 1
    else:
        cont_ma += 1
print('{} pessoas são maiores de idade e {} são menores de idade'.format(cont_ma, cont_me))

