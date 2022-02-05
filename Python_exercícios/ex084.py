# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.No final,
# mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lst = list()
temp = list()
while True:
    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite um peso: ')))
    if len(lst) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lst.append(temp[:])
    temp.clear()
    rep = str(input('Deseja continuar [S/N]: ').strip().upper())
    while rep not in 'SN':
        rep = str(input('COmando inválido. Deseja continuar [S/N]: '))
    if rep == 'N':
        break
print('-' * 30)
print(f'* O número de pessoas cadastradas foi: {len(lst)}')
print(f'* O maior peso cadastrado é: {mai}kg. Usuário(s) com esse peso:', end=' ')
for p in lst:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\n* O menor peso cadastrado é: {men}kg. Usuário(s) com esse peso:', end=' ')
for p in lst:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')

print(lst)



