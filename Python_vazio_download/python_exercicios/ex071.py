# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break




















# nota1 = 0
# nota10 = 0
# nota20 = 0
# nota50 = 0
# res = 0
# print('=' * 30)
# print(('{:^30}'.format('BANCO DO CIRÃO')))
# print('=' * 30)
# while True:
#     saque = int(input('Digite o valor a ser sacado: R$'))
#     if saque / 50 > 1:
#         nota50 = saque // 50
#         res = saque % 50
#         if res == 0:
#             break
#         if res / 20 > 1:
#             nota20 = res // 20
#             res = res % 20
#             if res == 0:
#                 break
#         if res / 10 > 1:
#             nota10 = res // 10
#             res = res % 10
#             if res == 0:
#                 break
#         if res / 1 > 1:
#             nota1 = res / 1
#             break
#     if saque / 20 > 1:
#         nota20 = saque // 20
#         res = saque % 20
#         if res == 0:
#             break
#         if res / 10 > 1:
#             nota10 = res // 10
#             res = res % 10
#             if res == 0:
#                 break
#         if res / 1 > 1:
#             nota1 = res // 1
#             break
#     if saque / 10 > 1:
#         nota10 = saque // 10
#         res = saque % 10
#         if res == 0:
#             break
#         if res / 1 > 1:
#             nota1 = res // 1
#             break
#     if saque / 1 >= 1:
#         nota1 = saque // 1
#         break
# if nota50 > 0:
#     print(f'Foram sacadas {nota50} notas de R$50')
# if nota20 > 0:
#     print(f'{nota20} notas de R$20')
# if nota10 > 0:
#     print(f'{nota10} notas de R$10')
# if nota1 > 0:
#     print(f'{nota1} notas de R$1')






