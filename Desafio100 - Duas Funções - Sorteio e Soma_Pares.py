from random import randint
from time import sleep
numeros = []


def sorteio():
    valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    print(f'Sorteando os {len(valores)} da lista: ', end='')
    sleep(2)
    print(f'{valores}')
    numeros.append(valores)


def soma_par():
    soma = 0
    for c in numeros[0]:
        if c % 2 == 0:
            soma += c
    print(f'Somando somente os valores pares da lista {numeros[0]}: ', end='')
    sleep(2)
    print(f'{soma}')


sorteio()
soma_par()
