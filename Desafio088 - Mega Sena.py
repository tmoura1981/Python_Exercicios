from random import randint
principal, secundaria = [], []
total_jogos = 1
titulo = 'Jogo da Mega Sena'
print('='*50)
print(f'{titulo.center(50)}')
print('='*50)
num_jogos = int(input('Quantos jogos quer fazer? '))
while total_jogos <= num_jogos:
    cont = 0  # contagem das dezenas de cada jogo
    while True:
        dezenas = randint(1, 60)
        if dezenas not in secundaria:
            secundaria.append(dezenas)
            cont += 1  # até ter 6 nºs em cada jogo
        if cont >= 6:
            break
    total_jogos += 1  # vai adicionado o total de jogos
    secundaria.sort()
    principal.append(secundaria[:])
    secundaria.clear()
print(f'Sorteando {num_jogos} jogos!!!')
print('='*50)
for indice, lista in enumerate(principal):
    print(f'Jogo {indice+1}: {lista}')
