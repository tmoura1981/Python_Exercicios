def ficha_jogador(n='<jogador desconhecido>', g=0):
    print(f'O jogador {n} marcou {g} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input(f'Quantos gol(s) {nome} marcou no campeonato? ')
if gols.isnumeric():
    gols = int(gols)  # transforma a str em int
else:
    gols = 0
if nome.strip() == '':  # verifica se há espaços antes e depois da str
    ficha_jogador(g=gols)
else:
    ficha_jogador(nome, gols)
