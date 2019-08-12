#peça p/ o programa quantos ns eram pares e impares
n = 1 #um nº q começa em 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n!= 0: #alguns não consideram 0 nem par nem ímpar
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vc digitou {} números pares e {} números ímpares.'.format(par, impar))
