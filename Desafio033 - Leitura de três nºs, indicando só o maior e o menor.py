#Leitura de três nºs, informando apenas qual é o maior e o menor.
n1 = int(input('\033[1;33mInforme o primeiro nº: \033[m'))
n2 = int(input('\033[1;33mInforme o segundo nº: \033[m'))
n3 = int(input('\033[1;33mInforme o terceiro nº \033[m'))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'\033[1;31mO maior nº é {maior}.\033[m')

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'\033[1;31mO menor nº é {menor}.\033[m')