def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Início de {inicio} até {fim} de {passo} em {passo}')
    print('=' * 60)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}  ', end='')
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}  ', end='')
            cont -= passo
    print('')
    print('')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Contagem Personalizada')
i = int(input('-> Início: '))
f = int(input('-> Fim: '))
p = int(input('-> Passo: '))
contagem(i, f, p)
