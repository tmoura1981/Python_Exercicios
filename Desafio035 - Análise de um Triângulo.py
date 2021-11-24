#As retas formam um triângulo?
#O maior lado do triângulo deve ser menor que a soma dos outros dois lados, considerando sempre os três lados.
r1 = int(input('Informe tamanho da primeira reta: '))
r2 = int(input('Informe o tamanho da segunda reta: '))
r3 = int(input('Informe o tamanho da terceita reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo.')

else:
    print('Não é possivel formar um triângulo.')