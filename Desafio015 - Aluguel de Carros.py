#Aluguel de Carro - Pgto à vista: 10% ou Parcelado em 3x c/ 5%

print('-' * 50)
km = float(input('\033[1;35mQual a quilometragem percorrida? \033[m'))
dias = int(input('\033[1;35mQuantos dias de aluguel? \033[m'))
preco = (60 * dias)+(0.15 * km)
print('-' * 50)
print(f'\033[1;36mCom quilometragem de {km:.2f} e o prazo de {dias} dias\né de R${preco:.2f}.\033[m')
print('-' * 50)
pgto = int(input('\033[1;36mÀ vista com 10% desc., digite [1]\nParcelado em 3x com 5% de desc.; digite [2] \033[m'))
if pgto == 1:
    preco *= 0.90
else:
    preco *= 0.95 / 3
print('-' * 50)
print(f'\033[1;35mO valor a ser pago é de R$ {preco:.2f}\33[m')
