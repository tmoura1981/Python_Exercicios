#Ler o nome completo de uma pessoa e:
#Nome com todas as letras maiúsculas.
nome = input('Qual o seu nome? ')
print(f'Tranformado em maiúsculo fica {nome.upper()}.')

#Nome com todas as letras minúsculas.
print(f'Transformando em minúsculo fica {nome.lower()}.')

#Quantas letras há ao todo, no nome e sobrenome, mas sem considerar os espaços?
print(f'A contagem somente de letras do nome e sobrenome, sem os espaços é {len(nome.replace(" ", ""))}')

#Quantas letras têm o primeiro nome?
dividido = nome.split()
print(f'O primeiro nome é {dividido[0]} e têm {len(dividido[0])} letras.')

#Quantas letras têm o segundo nome ou sobrenome?
print(f'O segundo nome ou sobrenome é {dividido[1]} e têm {len(dividido[1])} letras.')












