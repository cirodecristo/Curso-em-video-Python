# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))
print(f'Os valores digitados foram {valores}')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'* O maior valor da lista é {max(valores)} na posição {i}')
    elif v == min(valores):
        print(f'* O menor valor da lista é {min(valores)} na posição {i}')
