# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

import sys

print('-' * 50)
print('PRÓXIMOS 10 NÚMEROS DE UMA P.A')
print('-' * 50)
num = int(input('Digite um número da PA: '))
soma = 0
raz = int(input('Digite a razão da PA: '))
c = 0
lst = []
print('\nO primeiro número da PA é {} e sua razão {}, os próximos 10 números são: '.format(num, raz))
while c < 10:
    lst.append(num)
    num = num + raz
    print(num)
    c += 1
print(lst)
print(c)
print('FIM')
print('\n')
nt = int(input('Deseja mostrar mais termos desta PA? Digite [0] para sair ou o números de novos termos desejados: '))
nc = c + nt

while nt != 0:
    nc = c + nt
    while c < nc:
        lst.append(num)
        num = num + raz
        c += 1
        print(lst)
    nt = int(input('Você gostaria de mostrar mais termos desta PA? Digite [0] para sair ou o números de'
                   ' novos termos desejados: '))
print('FIM AMÉM SENHOR. O número de termos da PA é: {}'.format(len(lst)))
