from datetime import date  # poderia utizar from datetime import datetime
ano_atual = date.today().year  # datenow().year no lugar de date.today().year
dicionario = {}
for c in range(1):
    dicionario['Nome'] = input('Nome: ')
    ano_nasc = int(input('Ano de Nasc.: '))
    dicionario['Idade'] = ano_atual - ano_nasc
    dicionario['CTPS'] = int(input('Nº da CTPS (digite 0 caso não tenha): '))
    if dicionario['CTPS'] == 0:
        dicionario['CTPS'] = 'não possui'
        break
    else:
        dicionario['Ano de Contratação'] = int(input('Ano de Contratação: '))
        idade_aposentadoria = (dicionario['Ano de Contratação'] - ano_nasc)+35
        dicionario['Salário'] = int(input('Salário: R$ '))
        dicionario['Idade de Aposentadoria'] = idade_aposentadoria
print('=' * 55)
for k, v in dicionario.items():
    print(f'{k}: {v}')
