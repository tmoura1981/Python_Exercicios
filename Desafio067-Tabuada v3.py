print('-'*50)
while True:
    num = int(input('Digite um nº \033[1;31mpositivo\033[m para ver sua tabuada e \n\033[1;33mnegativo\033[m para encerrar: '))
    if num < 0:
        break
    print('-'*50)
    for c in range(1, 11):
        print(f'{num}x{c} = {num*c}')

    print('-'*50)
print('-'*50)
print('\033[1;33mTabuada Encerrada.\033[m')
