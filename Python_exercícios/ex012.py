preco = float((input('Digite o preço do produto: R$')))
desc_5 = preco * (5 / 100)
valor_desc = preco - desc_5

print('O valor do produto com 5% de desconto é de R${:.2f} \nParábens! Você economizou R${:.2f}'
      .format(valor_desc, desc_5))
