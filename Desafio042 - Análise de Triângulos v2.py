# Desafio 35 melhorado
# O maior lado do triângulo deve ser menor
# que a soma dos outros dois lados,
# considerando sempre os três lados.
print('-' * 50)
r1 = int(input('\033[1;34mInforme o tamanho da primeira reta: \033[m'))
r2 = int(input('\033[1;34mInforme o tamanho da segunda reta: \033[m'))
r3 = int(input('\033[1;34mInforme o tamanho da terceira reta: \033[m'))
print('-' * 50)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;35mCom as medidas acima, é possivel \nformar um triângulo\033[m', end='')
    if r1 == r2 == r3:
        print('\033[1;35m Equilátero.\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;35m Escaleno.\033[m')
    else:
        print('\033[1;35m Isósceles.\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo.\033[m')
print('-' * 50)
