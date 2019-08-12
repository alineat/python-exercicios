#from math import factorial
#n = int(input('Digite um nº p/ calcular seu fatorial: '))
#f = factorial(n)
#print('O fatorial de {} é {}.'.format(n, f))
#OU

n = int(input('Digite um nº p/ calcular seu Fatorial: '))
c = n #contador começa c/ n q é o numero q queremos fatorar
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))