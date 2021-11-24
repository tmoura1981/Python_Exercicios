titulo = 'Supermercados XXX'
print(titulo.center(50, '='))
nome_produto = ''
menor = preco_produto = total = qtd_produtos = contador = maior = 0
barato = resposta = caro = ''
while True:
    nome_produto = input('Digite o nome do produto: ').strip().upper()
    preco_produto = float(input('Digite o preço do produto: R$ '))
    resposta = input('Continuar [S] ou [N]? ').strip().upper()
    print('-' * 50)
    while resposta not in 'SN':
        resposta = input('Continuar [S] ou [N]? ').strip().upper()
    total += preco_produto
    contador += 1
    if preco_produto > 1000:
        qtd_produtos += 1
    if contador == 1 or preco_produto < menor:
        barato = nome_produto
        menor = preco_produto
    if contador == 1 or preco_produto > maior:
        caro = nome_produto
        maior = preco_produto
    if resposta == 'N':
        break
print(f'-> Total Gasto: R$ {total:.2f}.')
print('-'*50)
print(f'-> Total de Produtos acima de R$1000,00: {qtd_produtos}')
print('-'*50)
print(f'-> Nome do Produto mais barato: {barato} que custa R$ {menor}')
print('-'*50)
print(f'-> Nome do Produto mais caro: {caro} que custa R$ {maior}')
