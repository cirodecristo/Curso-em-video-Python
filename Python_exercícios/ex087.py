# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma1 = soma2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {mat[l][c]:^5} ]', end=' ')
        if mat[l][c] % 2 == 0:
            soma1 += mat[l][c]
        if c == 2:
            soma2 += mat[l][c]
        if l == 1:
            if mat[l][c] > maior:
                maior = mat[l][c]
    print()
print('-' * 30)
print(f'* A soma de todos os valores pares digitados: {soma1}')
print(f'* A soma dos valores da terceira coluna: {soma2}')
print(f'* O maior valor da segunda linha: {maior}')


