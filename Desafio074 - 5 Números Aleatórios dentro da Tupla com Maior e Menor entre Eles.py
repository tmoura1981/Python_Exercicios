from random import randint
conj_num = (randint(0, 5), randint(0, 10), randint(0, 15), randint(0, 20), randint(0, 25))
print('_'*50)
print(f'-> Os nºs sorteados foram {conj_num}')
print(f'-> O maior nº é {max(conj_num)}')
print(f'-> O menor nº é {min(conj_num)}')
print(f'-> Os nºs sorteados em ordem crescente: {sorted(conj_num)}')
print(f'-> Os nºs 1 e 5 aparecem entre os sorteados {conj_num.count(1)} vez e {conj_num.count(5)} vez.')
