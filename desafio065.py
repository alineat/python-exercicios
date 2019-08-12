resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um nº: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Vc digitou {} números e a média foi {}'.format(quant, media))
print(f'O maior valor foi {maior} e o menor foi {menor}.')