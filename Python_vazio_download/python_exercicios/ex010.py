wallet = float(input('Digite o valor contido na sua carteira: R$'))
dol = (wallet / 5.57)
eur = (wallet / 6.31)
print('Para a cotação de hoje, com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(wallet, dol, eur))