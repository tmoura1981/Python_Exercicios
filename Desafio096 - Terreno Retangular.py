def area(largura, comprimento):
    print('=' * 60)
    a = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {a:.2f}m²')


larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)
