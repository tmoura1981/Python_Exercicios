valores = [[], [], [],
           [], [], [],
           [], [], []]
num = linha = coluna = pos = soma = soma_ter_col = maior = 0
titulo = 'Matriz 3x3'
print(titulo.center(50, '='))
for v in range(9):  # 9 valores da matriz
    num = int(input(f'Linha[{linha}]   Coluna[{coluna}]: '))
    valores[pos].append(num)
    pos += 1
    coluna += 1
    if coluna == 3:  # após 3ª coluna
        coluna = 0  # volta à 1ª coluna
        linha += 1  # e desce à próxima linha de baixo
    if num % 2 == 0:
        soma += num
    if coluna == 0:
        soma_ter_col = valores[2] + valores[5] + valores[8]
print('_'*30)
print(f' {  valores[0]  }  {  valores[1]  }  {  valores[2]  } ')
print(f' {  valores[3]  }  {  valores[4]  }  {  valores[5]  } ')
print(f' {  valores[6]  }  {  valores[7]  }  {  valores[8]  } ')
print('_'*30)
print(f'-> Soma de todos os pares: {soma}')
print(f'-> Soma da 3ª coluna: {sum(soma_ter_col)}')
print(f'-> Maior nº da 2ª linha: {max(valores[3:6])}')  # pega-se o maior valor da 2ª linha
