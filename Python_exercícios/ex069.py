# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos

mul_20 = homem = mais_18 = 0
while True:
    print('-----CADASTRE UMA PESSOA-----')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite uma opção válida: [M/F]')).strip().upper()[0]
    if idade > 18:
        mais_18 += 1
    if sexo in 'F' and idade < 20:
        mul_20 += 1
    if sexo in 'M':
        homem += 1
    again = str(input('Deseja continuar? Digite [S] para sim e [N} para sair do programa: ')).strip().upper()[0]
    while again not in 'SN':
        again = str(input('Digite uma opção válida. [S] para continuar e [N] para sair: ')).strip().upper()[0]
    if again == 'N':
        break
print(f'A) {mais_18} pessoas tem mais de 18 anos\nB) {homem} homens cadastrados\nC) {mul_20} mulheres tem menos de 20'
      f' anos')

