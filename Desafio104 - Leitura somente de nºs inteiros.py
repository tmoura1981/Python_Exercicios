def num_inteiro(n=''):
    if n.isnumeric():
        n = int(n)
        print(f'O nº digitado foi {n}')
    else:
        print('Erro! Digite um nº inteiro!')


num = input('Digite um nº: ')
num_inteiro(num)
