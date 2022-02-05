from math import (cos, sin, tan,radians)
ang = int(input('Digite um ângulo:'))
coss = cos(radians(ang))
seno = sin(radians(ang))
tang = tan(radians(ang))

print('\nO ângulo digitado foi: {}°.\n*Seu cosseno é: {:.2f}\n*Seu seno é: {:.2f}\n*Sua tangente é: {:.2f}'
      .format(ang, coss, seno, tang))

