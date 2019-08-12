def avaliador_notas(n1, n2):
    media = (n1+n2) / 2
    if media >= 5:
        print('Passou')
    else:
        print('Recuperação')
    return media

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
nota = avaliador_notas(n1, n2)
print(nota)


"""n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('A sua nota é {:.1f}.'.format(media))
if media >= 6.0:
    print('Sua média foi boa, parabéns.')
else:
    print('Sua média foi baxa, estude mais.')"""