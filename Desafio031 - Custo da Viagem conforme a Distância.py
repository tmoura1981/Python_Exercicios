#Cálculo da distância x valor em uma viagem
distancia = int(input('Informe a distância da viagem: '))
if distancia <= 200:
    print('O valor a ser cobrado será de R$', distancia * 0.5)
else:
    print('O valor a ser cobrado será de R$', distancia * 0.45)