print('\033[1;35mProgressão Aritmética Versão 2\033[m')
print('-'*50)
prim_termo = int(input('\033[1;35mInforme o 1º termo da PA: \033[m'))
razao = int(input('\033[1;35mInforme a razão da PA: \033[m'))
termo = prim_termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'\033[1;35m{termo}\033[m')
        termo += razao
        cont += 1
    mais = int(input('\033[1;35mQuantos termos a mais você quer mostrar? \033[m'))
print('-'*50)
print(f'\033[1;35mO total de termos são {total}\033[m')