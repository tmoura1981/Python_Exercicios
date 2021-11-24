from random import randint
from time import sleep
print('-' * 50)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # computador escolhe uma das três opções.
print('\033[1;34m[0]Pedra', end=' ')
print('[1]Papel', end=' ')
print('[2]Tesoura')
print('')
usuario = int(str(input('\033[1;32mEscolha sua jogada: \033[m')))
if usuario != 0 and usuario != 1 and usuario != 2:
   print('\033[1;31mOpção Inválida! Jogue de 0 à 2.\033[m')
else:
   print('')
   print('\033[1;32mJO\033[m')
   sleep(1)
   print('\033[1;32mKEN\033[m')
   sleep(1)
   print('\033[1;32mPO\033[m')
   sleep(1)
   print('-' * 50)
   print(f'\033[1;36mComputador jogou {itens[computador]}!\033[m')
   print(f'\033[1;36mUsuário jogou {itens[usuario]}!\033[m')

if computador == 0:
   if usuario == 0:
      print('\033[1;33mEmpate!\033[m')
   elif usuario == 1:
      print('\033[1;33mUsuário venceu!\033[m')
   elif usuario == 2:
      print('\033[1;33mComputador venceu!\033[m')

elif computador == 1:
   if usuario == 0:
      print('\033[1;33mComputador venceu!\033[m')
   elif usuario == 1:
      print('\033[1;33mEmpate!\033[m')
   elif usuario == 2:
      print('\033[1;33mUsuário venceu!\033[m')

elif computador == 2:
   if usuario == 0:
      print('\033[1;33mUsuário venceu!\033[m')
   elif usuario == 1:
      print('\033[1;33mComputador venceu!\033[m')
   elif usuario == 2:
      print('\033[1;33mEmpate!\033[m')









