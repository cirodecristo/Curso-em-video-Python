# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lst = []
while True:
    val = int(input('Digite um valor: '))
    if val in lst:
        print('Valor já consta na lista')
    else:
        print('Valor adicionado com sucesso!!!')
        lst.append(val)
    novamente = str(input('Deseja continuar [S/N]? ').strip().upper())
    while novamente not in 'SN':
        novamente = str(input('Opção inválida. Deseja continuar [S/N]? ').strip().upper())
    if novamente == 'N':
        break
    else:
        continue
print(f'Você adicionou os seguintes números na sua lista {sorted(lst)}')




