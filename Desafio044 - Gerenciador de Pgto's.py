print('-' * 70)
valor = float(input('\033[1;34mQual o valor do produto? \033[m'))
print('-' * 70)
print('\033[1;34mFormas de pgto:\033[m')
pgto = int(input('\033[1;34m[1] À vista  \n[2] À vista no cartão  \n[3] 2x no cartão  \n[4] Acima de 3x no cartão \033[m'))
print('-' * 70)
if pgto <= 0 or pgto > 5:
    print('\033[1;31mInforme os códigos apenas de 1 à 4 para as formas de pgto!\033[m')
if pgto == 1:
    valor = valor * 0.90
    print(f'\033[1;34mO novo valor com 10% desconto será de R${valor:.2f}.\033[m')
elif pgto == 2:
    valor = valor * 0.95
    print(f'\033[1;34mO novo valor com 5% de desconto no cartão será \nde R${valor:.2f}.\033[m')
elif pgto == 3:
    valor = valor / 2
    print(f'\033[1;34mO valor das parcelas sem juros dividido no cartão \nserá de R${valor:.2f}.\033[m')
elif pgto == 4:
    parcela = int(input('\033[1;34mQuantas parcelas? \033[m'))
    valor = (valor * 1.20) / parcela
    print(f'\033[1;34mO valor das parcelas com juros \ndividido em {parcela} será de R${valor:.2f}.\033[m')
print('-' * 70)
