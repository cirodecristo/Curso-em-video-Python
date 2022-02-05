#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
#então o empréstimo será negado.

print('Bem-vindo(a) ao sistema de empréstimos do programa minha casa sua casa')
print('-' * 10)
cas = float(input('Digite o valor da casa que deseja comprar: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
ano = int(input('Digite em quantos anos deseja quitar a casa: '))
mes = ano * 12
pres = cas / mes
pres_max = sal * (30 / 100)

print('-' * 10)
print('\n1-O valor da casa desejada é: R${}\n2-O valor do seu salário é: R${:.2f}\n3-O número de anos para quitar o'
      ' imóvel é: {} anos ({} prestações)\n4-De acordo com seu salário, o valor máximo que você pode pagar em cada'
      ' prestação é: R${:.2f} (30% do seu salário)'
      .format(cas, sal, ano, mes, pres_max))
print('\n\n...ANALISANDO SEUS DADOS...')
if pres_max < pres:
    print('Empréstimo negado. O valor de cada prestação (R${:.2f}) excede 30% do seu salário.'.format(pres))
else:
    print('Empréstimo autorizado. O valor de cada prestação (R${:.2f}) não ultrapassa 30% do seu salário'. format(pres))

