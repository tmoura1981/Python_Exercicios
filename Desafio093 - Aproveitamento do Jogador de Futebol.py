dicionario = {}
gols = []
total_gols = gol = 0
dicionario['Nome do Jogador'] = input('Nome do Jogador: ')
dicionario['Nº de Partidas Disputadas'] = int(input(f'Nº de Partidas Disputadas pelo {dicionario["Nome do Jogador"]}: '))
x = dicionario.get('Nº de Partidas Disputadas')
print('='*30)
for c in range(0, x):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(gol)
    total_gols = sum(gols)
    dicionario['Gols'] = gols
    dicionario['Total de Gols'] = total_gols
print('='*30)
print(f'O jogador {dicionario["Nome do Jogador"]} fez {x} partidas.')
for c in range(0, x):
    print(f'=> Na partida {c+1} fez {gols[c]} gols')
print('='*30)
print(f'Total de {total_gols} gols.')