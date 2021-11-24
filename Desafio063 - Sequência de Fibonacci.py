print('\033[1;34mSequência de Fibonacci\033[m')
print('-'*50)
num = int(input('\033[1;34mQuantos termos da sequência você quer? \033[m'))
t1 = 0
t2 = 1
print(f'\033[1;33m{t1}->{t2}\033[m', end='')
contador = 3
while contador <= num:
    t3 = t1+t2
    print(f'\033[1;33m->{t3}\033[m', end='')
    contador += 1
    t1 = t2
    t2 = t3
print(f'\033[1;33m->Fim\033[m')
print('-'*50)
