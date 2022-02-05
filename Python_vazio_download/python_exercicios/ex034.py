#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o valor do salário: R$'))
aum1 = (sal * 10) / 100
aum2 = (sal * 15) / 100
nov_sal1 = sal + aum1
nov_sal2 = sal + aum2

if sal > 1250:
    print('-' * 10)
    print('Seu salário atual é de R${:.2f}.\nVocê recebeu 10% de aumento (+R${:.2f})\nSeu novo salário é'
          ' R${:.2f}'.format(sal, aum1, nov_sal1))
else:
    print('-' * 10)
    print('Seu salário atual é de R${:.2f}.\nVocê recebeu 15% de aumento (+R${:.2f})\nSeu novo salário é de'
          ' R${:.2f}'.format(sal, aum2, nov_sal2))
