# Soma entre nºs ímpares múltiplos de 3 entre 1 e 500.
soma = 0
contador = 0
print('-' * 50)
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1
        soma += i
print('A soma dos valores múltiplos\nde 3 entre 1 à 501 é {}.'.format(soma))
print('-' * 50)
print('A contagem de números entre 1 à 501\né de {}.'.format(contador))
print('-' * 50)





