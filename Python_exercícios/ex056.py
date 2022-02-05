# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from time import sleep
nome = []
idade = []
sexo = []
hom_velho = ''
idade_max = 0
mul_menos_20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p).strip())
    n = str(input('Digite o NOME da {}ª pessoa: '.format(p))).capitalize().strip()
    nome.append(n)
    i = int(input('Digite a IDADE da {}ª pessoa: '.format(p)))
    idade.append(i)
    s = str(input('Digite o SEXO da {}ª pessoa [M/F]: '.format(p))).upper().strip()
    sexo.append(s)
    if s == 'M' and idade_max < i:
        hom_velho = n
        idade_max = i
    if s == 'F' and i < 20:
        mul_menos_20 += 1
sleep(1)
print('\n...ANALISANDO DADOS...')
sleep(1)
print('\n* A média de idade do grupo é de: {} anos\n* O homem mais velho se chama: {} ({} anos)\n* Existem {}'
      ' mulher(es) com menos de 20 anos'.format(sum(idade) / 4, hom_velho, idade_max, mul_menos_20))


