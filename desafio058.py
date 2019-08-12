#from random import randint
#computador = randint(0, 10)
#jogador = int(input('Pensei em um número de 0 a 10, adivinhe qual foi: '))
#contador = 1
#while jogador != computador:
#    jogador = int(input('Você errou, tente de novo: '))
#    contador += 1
#print('Você acertou! Pensei no número {}. Após {}  tentativa(s), você acertou.'.format(computador, contador))

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um nº entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?' ))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas.'.format(palpites))