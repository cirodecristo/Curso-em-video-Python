# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

n = 0
fim = 'S'
lst = []
media = 0
c = 0

while fim == 'S':
    n = int(input('Digite um número: '))
    fim = str(input('Quer continuar? Digite [S] para continuar e [N] para sair: ')).strip().upper()
    while fim != 'S' and fim != 'N':
        fim = str(input('Insira uma opção válida. Digite [S] para continuar e [N] para sair: ')).strip().upper()
    if fim == 'N':
        print('FIM')
    lst.append(n)
    c += 1
media = sum(lst) / len(lst)
print('\n{} números digitados. A média é {}, o maior número é {} e o menor número é {}'.
      format(c, media, max(lst), min(lst)))


