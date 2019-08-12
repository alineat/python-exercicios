def avaliador_carro(tempo):
    if tempo <= 3:
        avaliacao = 'carro novo'
    else:
        avaliacao = 'carro velho'
    return avaliacao

idade_carro = int(input('Idade do carro: '))
resposta = avaliador_carro(idade_carro)
print(resposta)


"""SEM USAR FUNÇÃO
tempo = int(input('Há quantos anos você tem o seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')"""
