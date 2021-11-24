#Frequência da letra 'A'
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print(f'A letra "A" aparece {frase.count("a")} vezes.')

#Primeira vez que aparece a letra 'A'
print(f'A letra "A" aparece pela primeira vez na posição: {frase.find("a")+1}')

#Última aparicão da letra 'A'
print(f'A última aparição da letra "A" na frase é: {frase.rfind("a")+1}')
