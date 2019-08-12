maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1: #a priemira ocorrencia, o numero é maior e menor ja q ele ainda nao tem com q numero comparar
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso q eu li for maior q o maior, o maior passa a ser peso
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

