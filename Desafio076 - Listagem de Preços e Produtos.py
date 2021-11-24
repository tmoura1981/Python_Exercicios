titulo = 'Listagem de Produtos & Preços'
cabecalho = ('Produto', 'Preço')
real = 'R$'
produtos = ('Pão', 1.0, 'Leite', 4.5, 'Bolo', 3.0, 'Bolacha', 2.5, 'Pao de Queijo', 4.0, 'Suco', 2.5,
            'Café', 0.9, 'Pingado', 2.5, 'Pão Intregal', 8.5,)
print(titulo.center(50))
print('='*52)
for posicao, c in enumerate(cabecalho):
    if posicao % 2 == 0:
        print(f'{c}'.ljust(46), end='')
    elif posicao % 2 == 1:
        print(f'{c}')
for pos, i in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{i}'.ljust(45, '_'), end='')
    elif pos % 2 == 1:
        for cifrao in real:
            print(cifrao, end='')
        print(f' {i:.2f}')
print('='*52)
