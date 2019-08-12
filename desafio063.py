print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0 #pq o termo1 e o 2 são sempre 0 e 1
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3 #contador começa em 3 pq ja mostrei os 1º e 2ºtermo
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> Fim')
