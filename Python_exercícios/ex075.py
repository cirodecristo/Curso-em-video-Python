# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = 0
nums = (int(input('Digite um valor inteiro: ')), int(input('Digite um valor inteiro: ')),
        int(input('Digite um valor inteiro: ')), int(input('Digite um valor inteiro: ')))

print(f'* O valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'* O valor 3 apareceu na {nums.index(3) + 1}ª posição')
else:
    print('* O valor 3 não foi digitado')
while n < len(nums):
    if nums[n] % 2 == 0:
        print(f'Os números pares foram {nums[n]}', end=' ')
    n += 1

