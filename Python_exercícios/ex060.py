# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# num = int(input('Digite um número inteiro: '))
# c = num
# mult = 1
# print('Calculando {}!: '.format(num), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     if c > 1:
#         print(' x ', end='')
#     else:
#         print(' = ', end='')
#     mult = c * mult
#     c -= 1
# print(mult)
#
num = int(input('Digite um número inteiro: '))
c = num
mult = 1
for num in range(num, 0, -1):
    print('{}'.format(num), end='')
    if num > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    mult = num * mult
    num -= 1
print(mult)