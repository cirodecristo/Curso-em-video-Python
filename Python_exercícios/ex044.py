#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('LOJA DO CIRÃO'))
preco = float(input('Digite o preço do produto: R$ '))
print(('FORMAS DE PAGAENTO'))
condic = int(input('* Digite [1] para pagar à vista no dinheiro/cheque\n* Digite [2]'
                   ' para pagar à vista no cartão\n* Digite [3] para parcelar em 2x no cartão\n* Digite [4] para'
                   ' parcelar em 3x ou mais no cartão\n\nDigite a opção desejada:'))
if condic == 1:
    total = preco - (preco * 10 / 100)
    print('\nPARABÉNS! Você ganhou 10% de desconto. O valor a ser pago é: R${:.2f}'.format(total))
elif condic == 2:
    total = preco - (preco * 5 / 100)
    print('\nPARABÉNS! Você ganhou 5% de desconto. O valor a ser pago é: R${:.2f}'.format(total))
elif condic == 3:
    print('O valor a ser pago é: R${:.2f}'.format(preco))
elif condic == 4:
    parc = int(input('Digite o número de parcelas: '))
    total = preco + (preco * 20/100)
    print('Produto será parcelado em {}x, portando haverá um acréscimo de 20%. O valor a ser pago é:'
          ' R${:.2f} ({}x de R${:.2f})'.format(parc, total, parc, total / parc))
else:
    print('Opção de pagamento inválida')
