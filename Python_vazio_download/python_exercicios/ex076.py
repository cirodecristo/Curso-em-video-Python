prod_preco = ('Lápis', 2.31, 'Caderno', 35.30, 'Papel Sulfite', 15.50, 'Compasso', 5.20, 'Caneta', 3.00)
i = 0
print('=-' * 20)
print(f'{"PAPELARIA DO CIRÃO":^40}')
print('=-' * 20)
while i < len(prod_preco):
    print(f'{prod_preco[i]:.<30}', end='')
    i += 1
    print(f'R${prod_preco[i]:>7.2f}')
    i += 1
print('-' * 40)

