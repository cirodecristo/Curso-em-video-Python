from random import randint
jogos = int(input('Quantos jogos deseja fazer? '))
list_full = [[] for i in range(jogos)]
c = 0
while c < jogos:
    for n in range(0, 6):
        list_full[c].append(randint(1, 60))
    print(f'Jogo {c+1}: {list_full[c]}')
    c += 1
print('*' * 30, '\nBoa sorte!!!')


