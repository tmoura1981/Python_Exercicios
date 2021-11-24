#Ordem de Apresentação dos Alunos
import random
n1 = str(input('Informe seu nome: '))
n2 = str(input('Informe seu nome: '))
n3 = str(input('Informe seu nome: '))
n4 = str(input('Informe seu nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)



