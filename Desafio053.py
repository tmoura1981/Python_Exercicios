# Palindromo = frase ou palavra que pode
# ser lida de trás p/ frente
print('-' * 60)
frase = input(
    '\033[1;33mCite uma frase ou palavra\ne veja se é um palíndromo\033[m: ').strip()  # remove todos os espaçamentos.
print('-' * 60)
for i in range(1):
    frase = frase.lower()  # tranforma a frase toda em minúsculo.
    frase = frase.replace(' ', '')  # remove os espaços entre as palavras.
    frase = frase[::-1]  # lê a frase da direita p/ a esquerda.
if frase[0] == frase[-1]:
    print('\033[1;32mA frase ou palavra escolhida é um Palíndromo!\033[m')
else:
    print('\033[1;31mA frase ou a palavra escolhida não é um Palíndromo!\033[m')
print('-' * 60)
