#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input('Digite a distância da sua viagem em kms: '))
ticket = dist * 0.50
ticket2 = dist * 0.45

if dist <= 200:
    print('Sua passagem custará: R${:.2f}'.format(ticket))
else:
    print('Sua passagem custará: R${:.2f}'.format(ticket2))
