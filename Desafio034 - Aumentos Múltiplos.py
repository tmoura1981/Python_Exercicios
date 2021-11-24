#Salário com aumentos 10% ou 15%
salario = int(input('Informe seu salário: '))
if salario > 1250:
    print('O aumento é de R$', salario * 1.1)
else:
    print('O aumento é de R$', salario * 1.15)