import math

n1 = int(input('Digite um número:'))
n2 = n1 * 2
n3 = n1 * 3
nq = math.sqrt(n1)
nq2 = n1 ** (1/2)

print('O número digitado é: {} \nSeu dobro é: {} \nSeu triplo é: {} \nSua raiz quadrada é: {} ou {}'
      .format(n1, n2, n3, nq, nq2))