# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lst = []
for c in range(0, 5):
   v = int(input('Digite um valor: '))
   if c == 0 or v > max(lst):
       lst.append(v)
       print(f'Número adicionado no final da lista')
   else:
       pos = 0
       while pos < len(lst):
           if v <= lst[pos]:
               lst.insert(pos, v)
               print(f'Número adicionado na posição {pos}')
               break
           pos += 1
print(lst)
