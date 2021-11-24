# Ler 6 nºs inteiros e somar apenas os pares.
# Os ímpares serão ignorados na soma.
print('=' * 30)
s = 0
for i in range(1, 7):
    n = int(input('Digite um nº: '))
    if n % 2 == 0:
        s += n
print('=' * 30)
print('A soma somente dos pares é {}.'.format(s))

