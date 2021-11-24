valores = []
for c in range(5):
    numero = int(input('Valor: '))
    if c == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while True:
            if pos < valores[pos]:
                valores.insert(pos, numero)
            break
        pos += 1
print('_'*50)
print(f'Valores em ordem crescente: \n{valores}')
