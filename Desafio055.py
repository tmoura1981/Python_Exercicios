#Ler o peso de 5 pessoas e informar o maior e menor peso lidos.
print('-' * 30)
maior = 0
menor = 1000
for i in range(0,5):
    peso = int(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('-' * 30)
print('O menor peso é {}kg. \nO maior peso é {}kg.'.format(menor,maior))
print('-' * 30)