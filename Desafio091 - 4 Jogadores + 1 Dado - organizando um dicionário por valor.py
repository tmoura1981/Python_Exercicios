from operator import itemgetter  # fazer mais deste exercício com organização de dicionários
from time import sleep
from random import randint
print('Brindeira do Jogo de Dado')
print('='*30)
dicionario = {'Jogador 1': randint(1, 6),
              'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}
dicionario_ordenado = []
for k, v in dicionario.items():
    sleep(0.5)
    print(f'{k} tirou {v}')
print('='*30)
sleep(0.5)
print('Classificação dos Jogadores')
dicionario_ordenado = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for pos, c in enumerate(dicionario_ordenado):
    sleep(0.5)
    print(f'{pos+1}º lugar: {c[0]} com {c[1]}')
