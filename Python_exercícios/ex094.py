# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
cadastro = dict()
banco = list()
while True:
    cadastro['Nome'] = str(input('Digite o nome a ser cadastrado: '))
    cadastro['Sexo'] = str(input('Digite o sexo [M/F]: ').strip().upper())
    while cadastro['Sexo'] not in 'MF':
        cadastro['Sexo'] = str(input('Opção inválida. Digite o sexo [M/F]: ').strip().upper())
    cadastro['Idade'] = int(input('Digite a idade: '))
    banco.append(cadastro.copy())
    rep = str(input('Deseja cadastrar outro usuário [S/N]: ').strip().upper())
    while rep not in 'SN':
        rep = str(input('Opção inválida. Deseja cadastrar outro usuário [S/N]: ').strip().upper())
    if rep == 'N':
        break
soma = list()
mulheres = list()
acima_media = list()
media = sum(soma) / len(banco)
for c in range(0, len(banco)):
    soma.append(banco[c]['Idade'])
    if banco[c]['Sexo'] == 'F':
        mulheres.append(banco[c]['Nome'])
    if banco[c]['Idade'] > sum(soma) / len(banco):
        acima_media.append(banco[c])
print('-=' * 10)
print(f'* O total de usuários cadastrados é: {len(banco)}')
print(f'* A média de idade dos usuários cadastrados é: {sum(soma)/len(banco):5.2f}')
print(f'* O total de mulheres cadastradas é: {mulheres}')
print(f'* Foram cadastrados os seguintes usuários acima da média de idade: {acima_media}')
