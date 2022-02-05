# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.
from time import sleep
lst = list()
temp = list()
while True:
    aluno = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Digite a primeira nota do aluno(a): '))
    nota2 = float(input('Digite a segunda nota do aluno(a): '))
    media = (nota1 + nota2) / 2
    temp.append(aluno)
    temp.append([nota1, nota2])
    temp.append(media)
    lst.append(temp[:])
    temp.clear()
    rep = str(input('Deseja continuar [S/N]? ').strip().upper())
    while rep not in 'SN':
        rep = str(input('Opção INVÁLIDA! Deseja continuar [S/N]?'))
    if rep in 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
for c, l in enumerate(lst):
        print(f'{c:<4}{l[0]:<10}{l[2]:>8}')
print('-' * 30)
while True:
    nota3 = int(input('Deseja mostrar as notas individuais de algum aluno? Digite [999] para sair: '))
    if nota3 == 999:
        print('...ENCERRANDO...')
        sleep(1)
        break
    else:
        for c, l in enumerate(lst):
            if c == nota3:
                print(f'As notas de {l[0]} são: {l[1]}')
                print('-' * 30)


