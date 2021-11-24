from datetime import date
print('-' * 40)
menor = 0
maior = 0
for i in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    if date.today().year - ano_nasc >= 18:
        maior += 1
    else:
        menor += 1
print('-' * 40)
print('Os maiores de idade são {}. \nOs menores de idade são {}.'.format(maior, menor))
print('-' * 40)
