nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...\n')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem um total de: {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))


