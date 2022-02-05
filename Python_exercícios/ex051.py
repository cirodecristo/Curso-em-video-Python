# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.


# print('-' * 50)
# print('PRÓXIMOS 10 NÚMEROS DE UMA P.A')
# print('-' * 50)
#
# num = int(input('Digite um número da PA: '))
# raz = int(input('Digite a razão da PA: '))
#
# print('\nO primeiro número da PA é {} e sua razão {}, os próximos 10 números são: '.format(num, raz))
# for c in range(1, 11):
#     num = num + raz
#     print(num, end=' -> ')
# print('ACABOU')

print('-' * 50)
print('PRÓXIMOS 10 NÚMEROS DE UMA P.A')
print('-' * 50)

num = int(input('Digite um número da PA: '))
raz = int(input('Digite a razão da PA: '))
dec = num + (10 - 1) * raz

print('\nO primeiro número da PA é {} e sua razão {}, os próximos 10 números são: '.format(num, raz))
for c in range(num, dec + 3, raz):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
