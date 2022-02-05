sexo = str(input('Digite seu sexo [M/F]: ').upper())
while sexo != 'M' and sexo != 'F':
    print('Opção inválida, tente novamente')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
print('Sexo {} cadastrado!!!'.format(sexo))




