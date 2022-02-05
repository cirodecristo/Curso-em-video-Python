#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
#formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('-' * 10)
print('ANALISADOR DE TRÂNGULOS')
print('-' * 10)

r1 = float(input('Digite o tamanho da primeira reta em centímetros: '))
r2 = float(input('Digite o tamanho da segunda reta em centímetros: '))
r3 = float(input('Digite o tamanho da terceira reta em centímtros: '))
print('\n...ANALISANDO RETAS...')
print('-' * 10)

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print('A soma de dois dos lados é maior que o terceiro. É possível formar um triângulo.')
    print('-' * 10)
    if r1 == r2 == r3:
        print('Este é um triângulo equilátero. Todos os lados são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo isósceles. Dois lados são iguais')
    else:
        print('\nEste é um triângulo escaleno. Todos os lados são diferentes')
else:
    print('Não é possível formar um triângulo.')

