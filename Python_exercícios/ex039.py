#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
#alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime
print('SISTEMA DE ALISTAMENTO MILITAR')
print('-' *10)
sexo = str(input('Informe seu sexo. Digite "M" para masculino ou "F" para feminino:')).upper().strip()
ano_atual = datetime.today().year

if sexo == 'F':
    print('Alistamento não obrigatório')
    exit()
if sexo == 'M':
    ano = int(input('Informe seu ano de nascimento: '))
    idade = int(ano_atual) - ano
    if idade < 18:
        print('Calma jovem gafanhoto, você tem menos de 18 anos, ainda não é hora de se alistar. Ainda falta(m)'
              '{} ano(s) para seu alistamento'.format(18 - idade))
        print('Seu alistamento será em {}'. format(ano_atual + (18 - idade)))
    elif idade > 18:
        print('Você tem mais de 18 anos. Seu tempo de alistamento já passou. Já passaram {} ano(s) desde seu'
              ' alistamento'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano_atual - (idade - 18)))
    else:
        print('18 anos? Está na hora de se alistar')

