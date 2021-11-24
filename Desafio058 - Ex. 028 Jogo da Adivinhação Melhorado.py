# Exercício nº28 melhorado.
from random import randint
tentativa = 0
usuario = -1
computador = randint(0, 10)
print('-' * 50)
while usuario != computador:
    usuario = int(input('\33[1;36mEscolha um nº entre 0 à 10:\033[m '))
    if usuario > 10:
        print('\033[1;36mEscolha nºs apenas entre 0 à 10!\033[m')
        print('-' * 50)
    else:
        tentativa += 1
    if usuario == computador:
        print('-' * 50)
        print(f'\033[1;32mAcertou! Eu escolhi {computador} e você escolheu {usuario}.\033[m')
        print(f'\033[1;32mSuas tentativas foram {tentativa} vezes.\033[m')
print('-' * 50)

