#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
menor = num1
maior = num1

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    print('Você digitou números iguais, impossível definir maior e menor')
else:
    if (num2 < num1 and num2 < num3):
        menor = num2
    if (num3 < num1 and num3 < num2):
        menor = num3
    if (num2 > num1 and num2 > num3):
        maior = num2
    if (num3 > num1 and num3 > num2):
        maior = num3
    print('{} é o maior número e {} é o menor número.'.format(maior, menor))














