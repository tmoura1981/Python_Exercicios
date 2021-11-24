#Cálculo do comprimento catetos (oposto e adjacente) + comprimento da hipotenusa.
from math import hypot
print('-' * 60)
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = hypot(ca, co)
print('-' * 60)
print(f'A hipotenusa do cateto adjacente {ca} e do cateto oposto {co} é\n{h:.2f}.')
