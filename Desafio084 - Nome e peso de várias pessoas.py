pessoas, dados = [], []
while True:
    dados.append(input('Nome: '))  # 0
    dados.append(int(input('Peso: ')))  # 1
    pessoas.append(dados[:])
    dados.clear()  # limpa os dados da lista dados
    resp = input('Continuar? S/N: ').upper()
    print('='*50)
    if 'S' not in resp:  # estando dentro do loop, não precisa iniciar a variável
        break
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print('='*50)
#poderia colocar um contator no lugar do len(pessoas)
#mas seria mais uma variável, sendo desnecessário
print('Pessoas acima de 80 Kg:')
for c in pessoas:
    if c[1] >= 80:
        print(f'[{c[0]}]')
print('=' * 50)
print('Pessoas abaixo de 80 kg:')
for c in pessoas:
    if c[1] <= 80:
        print(f'[{c[0]}]')
