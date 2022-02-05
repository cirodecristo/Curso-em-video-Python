# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lst = []
while True:
    lst.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!!!')
    rep = str(input('Deseja continuar [S/N]: ').strip().upper())
    while rep not in 'SN':
        rep = str(input('Comando inválido. Deseja continuar [S/N]: ').strip().upper())
    if rep == 'N':
        break
    else:
        continue
print('-' * 10)
print(f'* A lista é: {lst}')
print(f'* Número de valores digitados: {len(lst)}')
lst.sort(reverse=True)
print(f'* Os valores ordenados em forma decrescente são: {lst}')
if 5 in lst:
    print('* O número 5 está presente na lista')
else:
    print('* O número 5 não está presente na lista')