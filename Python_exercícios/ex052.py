# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
mult = 0
for c in range(1, num + 1):
    if num % c == 0:
        mult += 1
        print('*{}*'.format(c), end=' -> ')
    else:
        print('{}'.format(c), end=' -> ')
if mult == 2:
    print('O número {} pode ser dividido somente {}x, logo, é primo'.format(num, mult))
else:
    print('O número {} pode ser dividido {}x , logo, não é primo'.format(num, mult))
print('FIM')
