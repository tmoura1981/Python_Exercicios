valores = []
while True:
    valores.append(int(input('Valor: ')))
    valores.sort(reverse=True)
    resposta = input('Continuar? [S]/[N] ').upper()
    if 'N' in resposta:
        break
print('_' * 50)
print(f'Os valores digitados foram {len(valores)}.')
print(f'Ordem decrescente dos valores: {valores}')
if 5 in valores:
    print(f'5 está na lista na posição {valores.index(5)}.')
else:
    print('5 não está na lista.')
