# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
performance = dict()
performance['Nome'] = str(input('Digite o nome do jogador: '))
performance['Partidas jogadas'] = int(input('Digite o número de partidas jogadas: '))
gols = list()
for p in range(0, performance['Partidas jogadas']):
    gols.append(int(input(f'Digite o número de gols marcados na {p + 1}o. partida: ')))
performance['Gols'] = gols[:]
performance['Gols no campeonato'] = sum(gols)
print('-=' * 30)
print(performance)
print('-=' * 30)
for k, v in performance.items():
    print(f'* O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {performance["Nome"]} jogou {performance["Partidas jogadas"]} partidas')
for p in range(0, performance['Partidas jogadas']):
    print(f'=> Gols na partida {p+1}: {performance["Gols"][p]}')
print(f'*** {performance["Nome"]} fez um total de {performance["Gols no campeonato"]} gols no campeonato')





# performance = dict()
# performance['Nome'] = str(input('Digite o nome do jogador: '))
# performance['Partidas jogadas'] = int(input('Digite o número de partidas jogadas: '))
# performance['Gols no campeonato'] = 0
# for p in range(0, performance['Partidas jogadas']):
#     performance[f'Gols na partida {p+1}'] = int(input(f'Digite o número de gols marcados na {p+1}o. partida: '))
#     performance['Gols no campeonato'] = performance['Gols no campeonato'] + performance[f'Gols na partida {p+1}']
# print(performance)