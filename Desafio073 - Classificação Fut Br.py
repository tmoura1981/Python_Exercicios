classificacao = 'Braga', 'Fortaleza', 'Palmeiras', \
                'Atlético-PR', 'Atlético-MG', 'Fluminense', \
                'Bahia', 'Atlético-GO', 'Flamengo', 'Corinthians'
print(f'Lista completa com todos os times: \n{classificacao}')
print('-'*50)
print(f'5 primeiros colocados: \n{classificacao[0:5]}')
print('-'*50)
print(f'4 últimos colocados: \n{classificacao[-4:]}')
print('-'*50)
print(f'Todos os times em ordem alfabética: \n{sorted(classificacao)}')
print('-'*50)
time = input('Qual time quer saber a posição? ')
if time in classificacao:
    print(f'O {time} está na posição {classificacao.index(time)+1}.')
print('')
posicao = int(input('Do 1º ao 10º, qual a posição quer saber? '))
print(f'Na posição {posicao}º está o {classificacao[posicao-1]}.')
