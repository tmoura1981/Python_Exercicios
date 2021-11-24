#Ler o nome, idade, sexo de 4 pessoas
#Mostrar a média de idade do grupo.
#Qual o nome do homem mais velho.
#Qtas mulheres têm menos de 20 anos.
soma_idades = 0
idade_homem_mais_velho = 0
mulheres_menos_vinte = 0
nome_homem_mais_velho = ''
print('-' * 50)
for a in range(0, 4):
    nome = input('Qual seu nome? ').strip()
    idade = int(input('Qual sua idade? '))
    sexo = input('Sexo: [M/F]: ').upper()
    print('-' * 50)
    soma_idades += idade
    if idade > idade_homem_mais_velho and sexo == 'M':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if idade < 20 and sexo == 'F':
        mulheres_menos_vinte += 1
media = soma_idades/4
print('\033[1;31mA média de idade do grupo é {:.2f}.\033[m'.format(media))
print('\033[1;31mO nome do homem mais velho é {}.\033[m'.format(nome_homem_mais_velho))
print('\033[1;31mMulheres com menos de 20 anos são ao todo {} pessoas.\033[m'.format(mulheres_menos_vinte))
print('-' * 50)
