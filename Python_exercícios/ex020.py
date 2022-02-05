from random import shuffle

a01 = input('Digite o nome do primeiro aluno:')
a02 = input('Digite o nome do segundo aluno:')
a03 = input('Digite o nome do terceiro aluno:')
a04 = input('Digite o nome do quarto aluno:')
lista = [a01, a02, a03, a04]
shuffle(lista)

print('A ordem de apresentação é: {}'. format(lista))
