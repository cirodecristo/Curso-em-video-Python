#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
#atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import datetime

ano = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.today().year
idade = ano_atual - ano

if idade <= 9:
    print('O atleta tem {} anos, portanto pertence a categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, portanto pertence a categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, portanto pertence a categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, portanto pertence a categoria SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos, portanto pertence a categoria MASTER'.format(idade))




