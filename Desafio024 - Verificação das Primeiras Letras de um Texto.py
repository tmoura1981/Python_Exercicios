#O nome da cidade começa ou não com Santo?
nome = str(input('Digite o nome de uma cidade: ')).strip() # strip: remove todos os espaçamentos desnecessários
                                                           # no início e no fim de uma cadeia de caracteres.
print('Santo' in nome.capitalize())


