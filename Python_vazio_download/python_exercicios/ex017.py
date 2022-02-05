from math import hypot

print('Vamos calcular o comprimento da hipotenusa do seu triângulo retângulo?')

cat_o = float(input('Primeiro, digite o comprimento do cateto oposto:'))
cat_a = float(input('Agora digite o comprimento do cateto adjacente:'))
hip = hypot(cat_a, cat_o)

print('O comprimento da hipotenusa é: {:.2f}'.format(hip))

