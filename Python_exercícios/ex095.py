# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
performance = dict()
jogadores = list()
gols = list()
c = 0
while True:
    performance['Id'] = c
    performance['Nome'] = str(input('Digite o nome do jogador: '))
    performance['Partidas'] = int(input('Digite o número de partidas jogadas: '))
    for p in range(0, performance['Partidas']):
        gols.append(int(input(f'Digite o número de gols marcados na {p + 1}o. partida: ')))
    performance['Gols'] = gols[:]
    performance['Gols no campeonato'] = sum(gols)
    jogadores.append(performance.copy())
    gols.clear()
    c += 1
    rep = str(input('Deseja continuar [S/N]? ').strip().upper())
    while rep not in 'SN':
        rep = str(input('Opção inválida! Deseja continuar [S/N]? ').strip().upper())
    if rep in 'N':
        break
print('-=-' * 30)
for k, v in performance.items():
    print(f'{str(k):<15}', end='')
print()
for i in jogadores:
    for k, v in i.items():
        print(f'{str(v):<15}', end='')
    print()
print('-=-' * 30)
while True:
    dados = int(input('Digite a [Id] do jogador para ver seus dados, caso deseje encerrar digite [999]: '))
    if dados == 999:
        print('...ENCERRANDO...', '\nFIM')
        break
    elif dados not in range(len(jogadores)):
        print(f'Número [Id] não consta na base de dados')
    else:
        if dados in range(len(jogadores)):
            print(f'LEVANTAMENTO DO JOGADOR {jogadores[dados]["Nome"]}')
            for p in range(0, jogadores[dados]['Partidas']):
                print(f'=> Gols na partida {p + 1}: {jogadores[dados]["Gols"][p]}')
            print('-=-' * 30)

