#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
#mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual é a velocidade atual do carro é? '))
exc = vel - 80
mul = exc * 7

if vel > 80:
    print('-' * 10)
    print('* Sua velocidade atual é {}kms/h. Você foi multado por excesso de velocidade.\n* Você está'
          ' {}kms/h acima da velocidade permitida.\n* Sua multa é: R${:.2f}.'.format(vel, exc, mul))
    print('-' * 10)
else:
    print('-' * 10)
    print('Você está dentro do limite de velocidade.')
print('Tenha um bom dia! Dirija com segurança.')
