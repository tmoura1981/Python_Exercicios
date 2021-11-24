print('-' * 50)
num = (int(input('Digite um 4º nº: ')),
        int(input('Digite um 4º nº: ')),
        int(input('Digite um 4º nº: ')),
        int(input('Digite um 4º nº: ')))
print('_'*50)
print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O nº 3 não consta entre os digitados.')
while True:
    print('Os pares são: ', end=' ')
    for c in num:
        if c % 2 == 0:
            print(f'{c}', end=' ')
    break


