frase = str(input('Digite uma frase qualquer: ').strip())
print('A letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra "A" aparece na posição {} na frase'.format(frase.upper().find('A')+1))
print('A última letra "A" aparece na posição {} na frase'.format(frase.upper().rfind('A')+1))

