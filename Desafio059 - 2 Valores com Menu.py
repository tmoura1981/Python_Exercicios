#programa com menus
sair_programa = 0
maior = 0
opcao = 0

print('-' * 50)
v1 = int(input('\033[1;32mInforme um valor: \033[m'))
v2 = int(input('\033[1;32mInforme outro valor: \033[m'))
print('-' * 50)

while sair_programa < 4:
    opcao = int(input('\033[1;32mEscolha uma das opções:\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Reset \n[5] '
                      'Sair\033[m '))
    if opcao == 1:
        print(f'\033[1;33mA soma entre os nºs é {v1+v2}.\033[m')
        print('-' * 50)
        continue
    elif opcao == 2:
        print(f'\033[1;33mO produto entre os nºs é {v1*v2}.\033[m')
        print('-' * 50)
        continue
    elif opcao == 3:
        maior = 0
        if v1 > maior:
            maior = v1
        if v2 > maior:
            maior = v2
        print(f'\033[1;33mO maior entre os nºs é {maior}.\033[m')
        print('-' * 50)
        continue
    elif opcao == 4:
        v1 = int(input('\033[1;33mEntre com um novo nº: \033[m'))
        v2 = int(input('\033[1;33mEntre com mais um novo nº: \033[m'))
        print('-' * 50)
    elif opcao == 5:
        print('\033[1;33mSaindo do sistema!\33[m')
        break
