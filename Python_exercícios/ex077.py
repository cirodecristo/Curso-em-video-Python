# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Carro', 'Praia', 'Navio', 'Onda')
for p in palavras:

    print(f'\nA palavra {p.upper()} contém as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
# v = 0
# l = 0
# vog = ''
# palavras = ('Carro'.upper(), 'Praia'.upper(), 'Navio'.upper(), 'Onda'.upper())
# while v < len(palavras):
#     while l < len(palavras[v]):
#         if palavras[v][l] in 'AEIOU':
#             vog += palavras[v][l] + ' '
#             l += 1
#         else:
#             l += 1
#     print(f'{palavras[v]} contém as seguintes vogais: {vog}')
#     l = 0
#     vog = ''
#     v += 1
# print(vog)






