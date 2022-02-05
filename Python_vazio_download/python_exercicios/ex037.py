#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro qualquer: '))
print('Escolha o número que corresponda a base de conversão desejada:')
base = int(input('Digite [1] para "BINÁRIO"\nDigite [2] para "OCTAL"\nDigite [3] pra "HEXADECIMAL"\n\nDigite um número: '))

if base == 1:
    print('{} convertido para binário equivale a: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal equivale a: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal equivale a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, digite um número entre 1 a 3')


