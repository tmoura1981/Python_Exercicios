limite = 80
velocidade = float(input('\033[1;34mInforme a velocidade do carro: \033[m'))
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f'\033[1;31mVocê será multado por ultrapassar o limite \nno valor de R$ {multa}.\033[m')
else:
    print('\033[1;32mVocê não será multado!\033[m')
