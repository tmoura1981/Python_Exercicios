from datetime import datetime
ano_nascimento = int(input('Informe o ano de seu nascimento: '))
ano_atual = datetime.today().year
dif = ano_atual - ano_nascimento
if dif < 18:
    print(f'Você ainda vai se alistar, \npois ainda faltam {18 - dif} anos.')
    print(f'O ano de seu alistamento será em {ano_nascimento + 18}')
elif dif == 18:
    print(f'Já está na hora de você se alistar, \npois você já tem {dif} anos.')
else:
    print(f'Seu tempo de se alistar já passaram {dif - 18} anos.')
    print(f'O ano do seu alistamento foi em {ano_nascimento + 18}.')
