num = int(input('\033[1;32mDigite um nº e veja seu fatorial: \033[m'))
cont = num
fatorial = 1
print('-' * 50)
while cont > 0:
    print(f'\033[1;33m{cont}\033[m', end='')
    print('\033[1;33mx\033[m' if cont > 1 else '\033[1;33m = \033[m', end='')
    fatorial *= cont
    cont -= 1
print(f'\033[1;33m{fatorial}\033[m')
print('-' * 50)




