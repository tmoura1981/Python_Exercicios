numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
for c in range(0, len(numero_extenso)):
    numero = int(input('Diga um nº de 0 à 10: '))
    print('-'*50)
    if 0 <= numero <= 10:  # nº está entre menor que 10 e maior que 0
        print(numero_extenso[numero])
        break
    else:
        print('Deve ser somente entre 0 e 10.')
