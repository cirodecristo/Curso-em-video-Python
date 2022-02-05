#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.

print('-' * 10)
print('ANALISADOR DE TRÂNGULOS')
print('-' * 10)

r1 = float(input('Digite o tamanho da primeira reta em centímetros: '))
r2 = float(input('Digite o tamanho da segunda reta em centímetros: '))
r3 = float(input('Digite o tamanho da terceira reta em centímtros: '))

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print('A soma de dois dos lados é maior que o terceiro. É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
