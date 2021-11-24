# Leitura do Sexo de uma pessoa
sexo = 'F' == 'M'  # Ou sexo = 'F' or 'M'
resposta = 'S'
while resposta == 'S':
    sexo = input('Sexo: [M] ou [F]: ').upper().strip()
    if sexo == 'F' or sexo == 'M':
        resposta = input('Deseja continuar? [S] ou [N]: ').upper()
    else:
        print('Resposta incorreta!')
