numero = soma = contador = 0
print('-' * 50)
while numero != 999:
    numero = int(input('\033[1;34mDigite um número qualquer diferente de 999: \033[m'))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'\033[1;34mA soma dos números foi {soma}.\033[m')
print(f'\033[1;34mO total de números digitados foram {contador}.\033[m')
print('-' * 50)
