print('\033[1;31mProgressão Aritmética\033[m')
print('-' * 50)
prim_termo = int(input('\033[1;33mInforme o 1º termo da PA: \033[m'))
razao = int(input('\033[1;33mInforme a razão da PA: \033[m'))
print('-' * 50)
termo = prim_termo
cont = 1
while cont <= 10:
    print(f'\033[1;32m{termo}->\033[m', end='')
    termo += razao
    cont += 1

