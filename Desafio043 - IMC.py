peso = float(input('\033[1;33mInforme seu peso: \033[m'))
altura = float(input('\033[1;33mInforme sua altura: \033[m'))
imc = peso/(altura * altura)
if imc < 18.5:
    print('\033[1;31mAbaixo do Peso!\033[m')
elif imc < 25:
    print('\033[1;36mPeso Ideal!\033[m')
elif imc < 30:
    print('\033[1;34mSobrepeso!\033[m')
elif imc < 40:
    print('\033[1;32mObesidade!\033[m')
elif imc > 40:
    print('\033[1;35mObesidade Mórbida!\033[m')