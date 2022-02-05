# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

lst = []
lst_par = []
lst_imp = []
c = 0
while True:
    lst.append(int(input('Digite um valor:')))
    rep = str(input('Deseja continuar [S/N]: ').strip().upper())
    while rep not in 'SN':
        rep = str(input('Comando inválido. Deseja continuar [S/N]').strip().upper())
    if rep == 'N':
        break
while c < len(lst):
    if lst[c] % 2 == 0:
        lst_par.append(lst[c])
        c += 1
    elif lst[c] % 2 == 1:
        lst_imp.append(lst[c])
        c += 1
print('-' * 10)
print(f'* A lista original é: {lst}')
print(f'* Os número pares da lista são: {lst_par}')
print(f'* Os número ímpares da lista são: {lst_imp}')



