# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
for a in range(0, 1):
    aluno['Nome'] = str(input('Digite o nome do aluno: '))
    aluno['Média'] = float(input('Digite a média do aluno: '))
    if aluno['Média'] <= 5:
        aluno['Situação'] = 'Reprovado'
    elif aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Aprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'* {k} do aluno: {v}')

print(f'* Nome do aluno: {aluno["Nome"]}\n* Média do aluno: {aluno["Média"]}\n* Situação do aluno: {aluno["Situação"]}')