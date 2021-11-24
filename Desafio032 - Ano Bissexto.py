# Verificar se um ano é ou não bissexto
from datetime import date
ano = int(input('Informar o ano desejado \nou aperte 0 (zero) para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # sinal de != sigfinica diferença em Python.
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
