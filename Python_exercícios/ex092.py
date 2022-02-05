# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Digite um nome: '))
cadastro['Ano de nascimento'] = int(input('Digite o ano de nascimento: '))
cadastro['Carteira de trabalho'] = int(input('Digite o n da carteira de trabalho [digite 0 caso não tenha]: '))
if cadastro['Carteira de trabalho'] != 0:
    cadastro['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o salário: '))
    cadastro['Idade'] = datetime.now().year - cadastro['Ano de nascimento']
    cadastro['Idade para aposentadoria'] = (cadastro['Ano de contratação'] + 35) - (cadastro['Ano de nascimento'])
print('-' * 30)
for k, v in cadastro.items():
    print(f'* {k}: {v}')
print('-' * 30)
print(f'ENCERRANDO')
print('-' *30)
