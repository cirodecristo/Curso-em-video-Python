# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {mat[l][c]:^5} ]', end=' ')
    print()






# mat = [[], [], [], [], [], [], [], [], []]
# p = 0
# for c in range(0, 9):
#     val = int(input(f'Digite o {c+1}.o valor para a matriz: '))
#     mat[p].append(val)
#     p += 1
# print(f'{mat[0]}, {mat[1]}, {mat[2]},\n{mat[3]}, {mat[4]}, {mat[5]},\n{mat[6]}, {mat[7]}, {mat[8]}')
