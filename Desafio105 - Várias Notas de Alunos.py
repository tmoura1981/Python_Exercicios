def notas_alunos(nota, show=False):
    qtd_notas = len(nota)
    maior_nota = max(nota)
    menor_nota = min(nota)
    media = sum(nota) / qtd_notas
    situacao = ''
    if media >= 7:
        situacao = 'Aprovado'
    elif 6 <= media <= 7:
        situacao = 'Recuperação'
    elif media < 6:
        situacao = 'Reprovado'
    dicionario = {'Total de Notas': qtd_notas, 'Maior Nota': maior_nota, 'Menor Nota': menor_nota, 'Média': media,
                  'Situacão': situacao}
    if show:
        print(f'-> O total de notas são {dicionario["Total de Notas"]}. \n-> A maior nota é {dicionario["Maior Nota"]}.'
              f'\n-> A menor nota é {dicionario["Menor Nota"]}.'f' \n-> A média é {dicionario["Média"]:.2f}'
              f'\n-> A situação é {situacao}.')
    else:
        print(f'-> O total de notas são {dicionario["Total de Notas"]}. \n-> A maior nota é {dicionario["Maior Nota"]}.'
              f'\n-> A menor nota é {dicionario["Menor Nota"]}.'f' \n-> A média é {dicionario["Média"]:.2f}')


p = int(input('Quantas notas quer exibir? '))
lista = []
for c in range(0, p):
    lista.append(float(input(f'{c+1}º Nota: ')))
notas_alunos(lista, show=True)
