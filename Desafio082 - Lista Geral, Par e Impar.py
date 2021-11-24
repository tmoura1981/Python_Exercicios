valores, pares, impares, resposta = [], [], [], 'S'
while True:
    valores.append(int(input('Valor: ')))
    resposta = input('Continuar? [S]/[N] ').upper()
    if 'S' not in resposta:
        break
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('_'*50)
print(f'Os valores são: {valores}')
print(f'Os pares são: {pares}')
print(f'Os ímpares são: {impares}')
