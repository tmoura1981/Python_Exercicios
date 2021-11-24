# ao colocar um import dentro da função, há economia de memória;
# neste caso, somente irá funcionar localmente e não de forma global
def voto(ano_nasc):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        print(f'Com {idade} de idade, é proibido votar.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} de idade, votar é opcional.')
    else:
        print(f'Com {idade} de idade, é obrigatório votar.')


nasc = int(input('Ano de Nasc.: '))
voto(nasc)
