print('\033[1;36m-\033[m' * 50)
a = float(input('\033[1;36mQual a altura da parede? \033[m'))
l = float(input('\033[1;36mQual a largura da parede? \033[m'))
print(f'\033[1;33mA área da parede é de {a*l:.2f} m².\033[m')
print(f'\033[1;33mA quantidade de tinta necessária para pintar esta parede é de {(a*l)/2:.2f} litros.\033[m')



