# Informe um nº e mostre sua tabuada
print('-' * 36)
n = int(input('Digite um nº e veja sua tabuada: '))
print('=' * 36)
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
print('=' * 36)
