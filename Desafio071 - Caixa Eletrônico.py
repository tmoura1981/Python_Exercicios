titulo = '\033[1;31mCaixa Eletrônico (ATM)\033[m'
print(titulo.center(50, '='))
print('')
qtd_nota = 0
valor = int(input('Valor a sacar: R$ '))
print('-' * 50)
total = valor
nota = 100
while True:
    if total >= nota:
        total -= nota
        qtd_nota += 1
    else:
        if qtd_nota > 0:
            print(f'Total de {qtd_nota} de R$ {nota}.')
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        qtd_nota = 0
        if total == 0:
            break
print('-' * 50)
