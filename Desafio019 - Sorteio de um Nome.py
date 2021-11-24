#Sorteio dos nomes dos alunos
import random
n1 = input('\033[1;32mQual o seu nome? \033[m')
n2 = input('\033[1;31mQual o seu nome? \033[m')
n3 = input('\033[1;33mQual o seu nome? \033[m')
n4 = input('\033[1;35mQual o seu nome? \033[m')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('-' * 50)
print(f'O nome sorteado é: {escolhido}')


