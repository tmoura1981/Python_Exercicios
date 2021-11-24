#Comparação entre dois números
n1 = int(input('\033[1;31mInforme um nº \033[m'))
n2 = int(input('\033[1;31mInforme um outro nº \033[m'))
if n1 > n2:
    print('\033[1;32mO primeiro número é maior que o segundo número.\033[m')
elif n1 < n2:
    print('\033[1;32mO segundo número é maior que o primeiro número.\033[m')
else:
    print('\033[1;32mNão existe valor maior, \npois ambos os números são iguais.\033[m')
