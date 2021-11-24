cont = soma = 0
while True:
    num = int(input('Digite um nº ou 999 para parar de vez: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'{cont} números foram digitados e a soma deles é {soma}.')
