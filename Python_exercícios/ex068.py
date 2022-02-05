# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
c = 0
while True:
    num_u = int(input('Digite um número inteiro: '))
    num_c = randint(1, 10)
    soma = num_u + num_c
    par_imp = str(input('Escolha par ou impar [P]/[I] : ')).strip().upper()
    if par_imp == 'P':
        if soma % 2 != 0:
            print(f'PERDEU. Você jogou {num_u} e o computador {num_c}. A soma entre eles é {soma}. NÚMERO ÍMPAR.')
            break
        elif soma % 2 == 0:
            print(f'VENCEU! Você jogou {num_u} e o computador {num_c}. A soma entre eles é {soma}. NÚMERO PAR!')
            print('Jogue novamente')
            c += 1
    if par_imp == 'I':
        if soma % 2 != 0:
            print(f'VENCEU! Você jogou {num_u} e o computador {num_c}. A soma entre eles é {soma}. NÚMERO ÍMPAR!')
            print('Jogue novamente')
            c += 1
        elif soma % 2 == 0:
            print(f'PERDEU. Você jogou {num_u} e o computador {num_c}. A soma entre eles é {soma}. NÚMERO PAR.')
            break
print(f'\nO jogo terminou. Você venceu {c} vezes')
