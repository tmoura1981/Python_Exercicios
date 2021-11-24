# Nºs primos
print('-' * 50)
tot = 0
n = int(input('Informe um nº inteiro e veja se ele é primo: '))
for c in range(1, n + 1):  # dentro do for sempre conta 1 a menos
    # por isso n+1 (Dica importante!)
    if n % c == 0:
        tot += 1  # se o nº for divisível soma mais 1 no total
        # é o mesmo que colocarmos tot = tot + 1

if tot == 2:  # se tot = 2 significa que o nº foi dividido 2x
    # e no caso dos nºs primos, essa é a regra.
    print('O nº{} é primo.'.format(n))
else:
    print('O nº{} não é primo.'.format(c))
print('-' * 50)
