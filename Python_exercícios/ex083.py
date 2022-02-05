# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
paren = []

exp = (str(input('Digite uma expressão matemática: '))).strip()
for c in exp:
    if '(' in c:
        paren.append(c)
    elif ')' in c:
        if '('in paren:
            paren.pop()
        else:
            paren.append(c)
print(paren)
if len(paren) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

