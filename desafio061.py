print('=-' * 6, '10 termos de uma PA', '-=' * 6)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 #contador começa c/1 p/mostrar os 10 primeiros termos
while cont <= 10:
    print(f'{termo} ->', end='')
    termo += razao
    cont += 1
print('Fim')
