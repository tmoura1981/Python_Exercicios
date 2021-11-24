valores = []
resp = 'S'
while resp == 'S':
    valores.append(int(input('Digite um nº: ')))
    for c in valores:
        if valores.count(c) > 1:
            print('Duplicado! Este valor não será registrado!')
            valores.pop()
    resp = input('Continuar? [S]/[N] ').upper()
    print('-' * 30)
print('-> Valores registrados com sucesso!')
print(f'-> Todos os valores digitados em ordem crescente foram \n{sorted(valores)}')
