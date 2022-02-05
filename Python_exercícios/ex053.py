# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
# espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

fra = str(input('Digite uma frase: ')).strip().upper()
pal = fra.split()
print(pal)
jun = ''.join(pal)
print(jun)
inv = jun[::-1]
'''for let in range(len(jun) - 1, -1, -1):
    inv = inv + jun[let]
print('O inverso de {} é {}'.format(jun, inv))'''

if jun == inv:
    print('{} é um palíndromo'.format(fra))
else:
    print('{} não é um palíndromo'.format(fra))
