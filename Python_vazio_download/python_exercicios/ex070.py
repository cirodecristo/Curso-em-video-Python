# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

preco_lst = []
prod1000_lst = []
preco_bar = 0
prod_bar = ''

while True:
    prod = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$ '))
    preco_lst.append(preco)
    if preco_bar == 0 or preco < preco_bar:
        preco_bar = preco
        prod_bar = prod
    if preco > 1000:
        prod1000_lst.append(prod)
    cont = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Opção inválida. Escola [S] para continuar e [N] para sair: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'A) O valor total da compra foi R${sum(preco_lst)}\nB) {len(prod1000_lst)} produtos custaram mais que R$1000\n'
      f'C) O produto mais barato foi {prod_bar} e custou R${preco_bar}')
