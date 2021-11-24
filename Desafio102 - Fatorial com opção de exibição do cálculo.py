def fatorial(n=1, show=False):
    """
    Cálculo de fatorial
    :param n: nº a ser calculado seu fatorial
    :param show: False: não exibe o cálculo / True: exibe o cálculo
    :return: retorna o resultado do fatorial
    """
    if not show:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end=' x ')
        print('\b\b', end='= ')

        return f


print('=' * 30)
num = int(input('Digite um nº: '))
while True:
    mostrar_calculo = input('Mostrar cálculo? [S/N] ').upper()
    if mostrar_calculo in 'SN':
        break
    print('Informar somente S ou N.')
if 'S' in mostrar_calculo:
    print(fatorial(num, show=True))
else:
    print(fatorial(num, show=False))
help(fatorial)
