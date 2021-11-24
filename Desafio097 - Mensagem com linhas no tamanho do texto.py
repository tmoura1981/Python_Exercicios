def escreva(msg):
    tam = 0
    if tam <= len(msg):
        tam = 2 + len(msg)
        print('='*tam)
        print(msg.center(tam))
        print('='*tam)
    print('')


palavra1 = input('Digite algo: ')
palavra2 = input('Digite algo: ')
escreva(palavra1)
escreva(palavra2)
