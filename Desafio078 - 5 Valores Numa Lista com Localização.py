valores = []
for c in range(5):
    valores.append(int(input(f'Digite um nº para posição {c}: ')))
print('_'*50)
print(f'Os valores digitados são {valores}')
print(f'O maior valor é {max(valores)} na(s) posição(ões) ', end='')
for pos, i in enumerate(valores):
    if i == max(valores):
        print(f'{pos}->', end=' ')
print('')
print(f'O menor valor é {min(valores)}, na(s) posição(ões) ', end='')
for pos, i in enumerate(valores):
    if i == min(valores):
        print(f'{pos}->', end=' ')


