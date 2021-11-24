from random import randint
print('\033[1;33mJogo do Par ou Impar\033[m')
print('-' * 50)
opcao = ''
comput = randint(0, 5)
total = cont = 0
while True:
    user = int(input('\033[1;33mDiga um valor: \033[m'))
    opcao = input('\033[1;33m[P] Par ou [I] Impar? \033[m').upper().strip()[0]
    while opcao not in 'PI':  #enquanto opção não tiver P e I
        opcao = input('\033[1;33m[P] Par ou [I] Impar? \033[m').upper().strip()[0]
    total = user + comput
    if total % 2 == 0:
        print(f'\033[1;33mVocê jogou {user} e o computador jogou {comput}. Total deu {total}.\033[m')
        if opcao == 'P':
            print('\033[1;33mVocê ganhou. Vamos jogar novamente.\033[m')
            cont += 1
            print('-' * 50)
            user = True
            continue
        else:
            print(f'\033[1;31mPerdeu! Você venceu apenas {cont} vez(es).\033[m')
            break
    elif total % 2 == 1:
        print(f'\033[1;33mVocê jogou {user} e o computador jogou {comput}. Total deu {total}.\033[m')
        if opcao == 'I':
            print('\033[1;33mVocê ganhou. Vamos jogar novamente.\033[m')
            cont += 1
            print('-' * 50)
            user = True
            continue
        else:
            print(f'\033[1;31mPerdeu! Você venceu apenas {cont} vez(es).\033[m')
            break
