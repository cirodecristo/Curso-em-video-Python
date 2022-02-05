# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-' * 10)
    n = int(input('Digite um número para ver sua tabuada, caso deseje finalizar, digite um número negativo: ').strip())
    print('-' * 10)
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1
print('fim')
