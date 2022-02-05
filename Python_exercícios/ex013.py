salario = float(input('Digite seu salário atual: R$'))
aumento = salario * (15 / 100)
new_salario = salario + aumento

print('Seu salário atual é: R${:.2f} \nParabéns! Você recebeu um aumento de: R${:.2f} \nSeu novo salário é: R${:.2f}'
      .format(salario, aumento, new_salario))