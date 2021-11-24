#Média do Aluno
n1 = float(input('\033[1;35mInforme a primeira nota: \033[m'))
n2 = float(input('\033[1;35mInforme a segunda nota: \033[m'))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'\033[1;31mReprovado! Pois, sua média foi {m:.2f}\033[m')
elif m < 6.9:
    print(f'\033[1;33mRecuperação! Estude mais, pois, sua média foi {m:.2f}\033[m')
else:
    print(f'\033[1;36mAprovado! Parabéns, sua média foi {m:.2f}\033[m')
