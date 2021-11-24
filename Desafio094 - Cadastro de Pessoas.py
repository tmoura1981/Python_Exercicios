pessoas = {}
lista_pessoas, idades, mulheres = [], [], []
while True:
    print('='*55)
    pessoas['Nome'] = input('Nome: ').capitalize()
    while True:
        pessoas['Sexo'] = input('Sexo M/F: ')
        if pessoas['Sexo'] in 'mf':
            break
        print('Digite apenas M/F.')
    if pessoas['Sexo'] == 'm':
        pessoas['Sexo'] = 'Masculino'
    elif pessoas['Sexo'] == 'f':
        pessoas['Sexo'] = 'Feminino'
        mulheres.append(pessoas['Nome'])
    pessoas['Idade'] = int(input('Idade: '))
    idades.append(pessoas['Idade'])
    lista_pessoas.append(pessoas.copy())
    media_idade = sum(idades) / len(lista_pessoas)
    while True:
        resposta = input('Continuar? S/N ').upper()
        if resposta in 'SN':
            break
        print('Digite apenas S/N.')
    if 'S' not in resposta:
        break
print('='*55)
print(f'-> O grupo têm {len(lista_pessoas)} pessoas.')
print(f'-> A média de idade é {media_idade:.2f}.')
print(f'-> As mulheres do grupo são: {mulheres}')
print('-> Lista de pessoas com a idade acima da média:')
for acima_da_media in lista_pessoas:
    if acima_da_media['Idade'] > media_idade:
        print(f'Nome: {acima_da_media["Nome"]}  Sexo: {acima_da_media["Sexo"]}  Idade: {acima_da_media["Idade"]}')
