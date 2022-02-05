# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO','Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport', 'Chapecoense')

print('=-=' * 10)
print('TABELA DO BRASILEIRÃo 2022')
print(f'{times}')
print('=-=' * 10)
print(f'* 5 primeiros colocados: {times[:5]}')
print(f'* 4 últimos colocados: {times[-4:]}')
print(f'* Times em ordem alfabética: {sorted(times)}')
print(f'* Posição da Chapecoense: {times.index("Chapecoense") + 1}ª colocado')
