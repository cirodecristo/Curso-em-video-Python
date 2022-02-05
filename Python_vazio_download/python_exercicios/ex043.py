#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
#Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: (kg) '))
alt = float(input(('Digite sua altura: (m) ')))
imc = peso / (alt ** 2)
print('-' * 10)
print('\nSeu IMC é: {:.1f} kg/m²'.format(imc))

if imc < 18.5:
    print('Procure se alimentar melhor, você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está na faixa de de PESO IDEAL')
elif 25 <= imc < 30:
    print('Atente-se, você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Cuidado! Você está em OBESIDADE')
elif imc >= 40:
    print('PROCURE UM PROFISSIONAL! Você está em OBESIDADE MÓRBIDA')




