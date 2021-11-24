from random import randint
from time import sleep


def maior(*num):  # sinal de * faz o desempacotamento dos parâmetros
    sleep(0.6)
    print(f'Os valores informados são {len(num)}: ', end='')
    sleep(0.6)
    print(num)
    sleep(0.6)
    print(f'O maior valor entre os {len(num)} nºs é: {max(num)}')
    print('='*60)


maior(randint(0, 100), randint(0, 500), randint(0, 1000))
maior(randint(0, 50), randint(0, 100))
maior(randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
maior(randint(0, 5))
