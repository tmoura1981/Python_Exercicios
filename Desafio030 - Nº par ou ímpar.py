#Verificar se um nº é par ou impar.
n = int(input('Digite um nº: '))
resto = n % 2
if resto == 0:
    print('O nº escolhido é par.')
else:
    print('O nº escolhido é impar.')