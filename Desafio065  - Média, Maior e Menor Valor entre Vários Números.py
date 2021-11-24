menor = 1000
numero = soma = media = maior = contador = 0
resposta = 'S'
print('-' * 50)
while resposta == 'S':
    numero = int(input('\033[1;36mDigite um número qualquer: \033[m'))
    soma += numero
    contador += 1
    media = soma/contador
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    resposta = input('\033[1;36mContinuar? [S] ou [N]: \033[m').upper()
print('-' * 50)
print(f'\033[1;36mO maior nº digitado de todos é {maior}.\033[m')
print(f'\033[1;36mO menor nº digitado de todos é {menor}.\033[m')
print(f'\033[1;36mA média entre todos os nºs é {media:.2f}.\033[m')
print(f'\033[1;36mAo todo foram digitados {contador} nºs.\033[m')
print('-' * 50)
