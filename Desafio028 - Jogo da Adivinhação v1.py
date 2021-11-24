# Jogo de adivinhação de um nº.

from random import randint
print('-' * 70)
computador = randint(0, 5)  # Aqui o computador "pensa e sorteia" um nº.
usuario = int(input('\033[1;36mEscolha um nº somente entre 0 à 5: \033[m'))  # O nº escolhido pelo usuário.
if usuario == computador:
    print(f'\033[1;33mVocê acertou! Parabéns! Seu nº é {usuario} \ne o escolhido por mim, também é {computador}.\033[m')
else:
    print(f'\033[1;31mVocê errou! O nº escolhido por mim foi {computador}.\033[m')
print('-' * 70)
