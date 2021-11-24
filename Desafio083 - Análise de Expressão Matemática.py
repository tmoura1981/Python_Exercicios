titulo = 'Analizador de Expressões Matemáticas'
print(titulo.center(50))
expressao = input('Expressão matemática: ')
lista = []
for sinal in expressao:
    if sinal == '(':
        lista.append('(')
    elif sinal == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
