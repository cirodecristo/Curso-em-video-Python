# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# c = 0
# num = int(input('Digite um número entre 0 e 20: '))
# while num > 20 or num < 0:
#     num = int(input('Tente novamente!!! Digite um número entre 0 e 20: '))
# while c != num:
#     c += 1
# print(numeros[c])

c = 0
while True:
    num = int(input('Digite um número entre 0 e 20, digite [999] para encerrar o programa: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente')
while c != num:
        c += 1
print(f'Você digitou o número {numeros[c]}')
