total = totmil = menor = cont = 0
barato = '' #poduto barato começa c/vazio pq ainda ñ tenho nenhum produto
while True: #enquanto infinito
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    #else: # coloquei no or pq é a mesma coisa.
     #  if preco < menor:
     #       menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:10.2f}') #10 casas e duas casas flutuantes
print(f'Temos {totmil} produtos custando mais de mil reais.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')