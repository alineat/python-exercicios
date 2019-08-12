# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'. Foram informados {cont} valor(es).') # ou len(num)
    print(f'O maior valor informado foi {maior}') # ou max(num)


maior(1, 7, 5)
maior(2, 0, -2)
maior(80, 1, 2, 5, 2, 10)
maior()
