# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag).

soma = c = 0
while True:
    n = int(input('Digite um número, use [999] para parar: '))
    if n == 999:
        break
    soma += + n
    c += 1
print(f'{c} números digitados. A soma é: {soma}')