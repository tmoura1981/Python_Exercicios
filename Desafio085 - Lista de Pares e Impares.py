valores = [[], []]
num = 0
for c in range(7):
    num = int(input(f'{c + 1}º Valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('='*50)
print(f'Pares: {sorted(valores[0])}')
print(f'Impares: {sorted(valores[1])}')
