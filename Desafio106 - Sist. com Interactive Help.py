from time import sleep


def socorro(com):
    help(com)


def titulo(msg='Sistema de Ajuda'):
    tam = 0
    if tam <= len(msg):
        tam = 5 + len(msg)
        print('\033[7;30;44m-\033[m'*tam)
        print(f'\033[7;30;44m{msg.center(tam)}\033[m')
        print('\033[7;30;42m-\033[m'*tam)


titulo()
while True:
    opcao = int(input('[1] Função/Biblioteca\n[2] Fim '))
    if opcao == 1:
        escolha_funcao = input('Nome da Função/Biblioteca: ')
        print('Searching', end='')
        for c in range(3):
            sleep(0.5)
            print('.', end='')
        print('')
        sleep(3)
        titulo(f'Acessando o manual do comando <{escolha_funcao}>')
        socorro(escolha_funcao)
        titulo()
    elif opcao == 2:
        break
