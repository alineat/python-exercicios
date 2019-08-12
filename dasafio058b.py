from random import randint
computador = randint(0, 10)
jogador = int(input('Pensei em um número de 0 a 10, adivinhe qual foi: '))
contador = 1
while jogador != computador:
    print('Você errou.')
    if jogador < computador:
        jogador = int(input('Mais... Tente mais uma vez: '))
    elif jogador > computador:
        jogador = int(input('Menos... Tente mais uma vez: '))
    contador += 1
print('Você acertou! Pensei no número {}. Você acertou na {}ª tentativa.'.format(computador, contador))
