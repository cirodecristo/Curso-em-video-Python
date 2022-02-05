# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.

lista = []
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    lista.append(peso)
peso_max = max(lista)
peso_min = min(lista)
print('{}kg é o MAIOR peso'.format(peso_max))
print('{}kg é o MENOR peso'.format(peso_min))

