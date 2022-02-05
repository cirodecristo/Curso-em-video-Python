# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.

num = [[], []]
for n in range(0, 7):
    val = int(input(f'Digite o {n+1}º valor: '))
    if val % 2 == 0:
        num[0].append(val)
    elif val % 2 == 1:
        num[1].append(val)
num[0].sort()
num[1].sort()
print(f'* Os valores PARES são: {num[0]}')
print(f'* Os valores ÍMPARES são: {num[1]}')