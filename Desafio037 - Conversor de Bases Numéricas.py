# Base de Conversão
n = int(input('Favor informar um nº: '))
print('''Escolha uma das bases para a conversão:

[1] Binário
[2] Octal
[3] Hexadecimal
''')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    print(f'O número {n} em Binário fica {bin(n)[2:]}.')
elif opcao == 2:
    print(f'O número {n} em Octal fica {oct(n)[2:]}.')
elif opcao == 3:
    print(f'O número {n} em Hexadecimal fica {hex(n)[2:]}.')
else:
    print('Opção inválida! Escolha as opções de 1 à 3!')
