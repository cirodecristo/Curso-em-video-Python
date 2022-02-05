# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

print('-' * 50)
print('PRÓXIMOS 10 NÚMEROS DE UMA P.A')
print('-' * 50)

num = int(input('Digite um número da PA: '))
raz = int(input('Digite a razão da PA: '))
c = 0
print('\nO primeiro número da PA é {} e sua razão {}, os próximos 10 números são: '.format(num, raz))
while c < 10:
    print('{}'.format(num), end=' -> ')
    num = num + raz
    c += 1
print('ACABOU')