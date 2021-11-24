#1º termo e a razão de uma progressão aritmética
#an = a1 + (n-1)r
#an = termo a calcular
#a1 = 1º termo da PA (é cada número, independente da ordem)
#n = posição do termo a descobrir(1º,2º,3º...)
#r = razão (difença entre cada um dos termos)
print('--' * 25)
a1 = int(input('1-Qual o 1º termo da PA? '))
n = int(input('2-Qual a posição do termo da PA: '))
r = int(input('3-Informe a razão da PA: '))
for i in range(1, 11):
    an = a1 + (n-1) * r
print('--' * 25)
print('-> O {}º termo da PA é igual à {}.'.format(n, an))
print('--' * 25)
print('-> Os termos da PA são:'.format(n))
for i in range(a1, an+r, r):
    print(i)
print('--' * 25)
