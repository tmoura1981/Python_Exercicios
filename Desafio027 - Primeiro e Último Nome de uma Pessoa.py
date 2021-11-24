#Ler apenas o primeiro e o último nome de uma pessoa.
nome = str(input('Qual o seu nome completo? ')).strip()
dividido = nome.split()
print(f'Primeiro nome: {dividido[0]}')
print(f'Último nome: {dividido[len(dividido)-1]}')



