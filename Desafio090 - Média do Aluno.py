alunos = {}
alunos['Nome'] = input('Nome: ')
alunos['Média'] = int(input('Média: '))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos['Média'] < 7:  # está entre 5 e 7. Praticar esta estrutura de faixa de valores
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print('='*30)
for k, v in alunos.items():
    print(f'{k} = {v}')
