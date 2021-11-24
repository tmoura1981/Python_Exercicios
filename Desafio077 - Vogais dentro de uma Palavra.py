palavras = ('carro', 'bicicleta', 'caminhão', 'patins', 'ônibus', 'trem',
            'avião', 'Thiago', 'casa', 'programação')
print('_'*50)
for c in palavras:
    print(f'\n-> Na palavra {c}, temos a vogais: ', end='')
    for vogais in c:
        if vogais.lower() in 'aáãeéiíoóôuú':
            print(f'{vogais}', end=' / ')
    print('\b\b', end='')
print('')
