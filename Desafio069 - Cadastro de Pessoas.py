titulo = 'Cadastro de Pessoas'
print(titulo.center(50, '='))
print('')
idade = total = homens = mulheres = 0
sexo = ''
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M] ou [F]? ').upper().strip()[0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M] ou [F]? ').upper().strip()[0]
    resposta = input('Continuar? [S] ou [N] ').upper().strip()[0]
    while resposta not in 'SN':
        resposta = input('Continuar? [S] ou [N] ').upper().strip()[0]
    print('-' * 50)
    if idade >= 18:
        total += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if resposta == 'N':
        break
print(f'Total de maiores de 18 anos: {total}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres menores de 20 anos: {mulheres}')
