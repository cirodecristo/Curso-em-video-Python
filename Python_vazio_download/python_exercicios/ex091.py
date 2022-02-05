# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from random import randint
from operator import itemgetter
jogadores = dict()
ranking = list()
for c in range(0, 4):
    jogadores[f'Jogador {c + 1}'] = randint(0, 6)
print(jogadores)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]} no dado')