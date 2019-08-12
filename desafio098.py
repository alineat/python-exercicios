# Faça um programa que tenha uma função chamada contador(), que receba 3 parâmemtros: início, fim e passo. Seu programa
# tem que realizar 3 contagens através da funçãao criada: a) de 1 até 10, de 1 em 1. b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada.
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1 # se passo for menor q zero, deixe ele positivo
    if passo == 0:  # se o passo for zero, transforme ele em 1.
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(0.2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True) #use <, flush=True> se vc estiver c/ a última versão do Pycharm, p/ sleep
            sleep(0.2)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Início da contagem: '))
fin = int(input('Final da contagem:  '))
pas = int(input('Passo da contagem:  '))
contador(ini, fin, pas)