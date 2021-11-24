#Nº pares de 1 à 50
from time import sleep
print('\033[1;32mPares de 1 à 50:\033[m')
print('-' * 155)
for c in range(2, 51, 2):
    print(c, '-', end=' ')
    sleep(0.3)


