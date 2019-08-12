# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
'''Minha resposta
def fatorial(numero_calcular=1):
    cont = 1
    for n in range(numero_calcular, 0, -1):
        cont = cont * n
        if n >= 2:
            print(f'{n} * ', end='')
        else:
            print(f'{n}', end='')
    return f' = {cont}'


print(fatorial(5))
'''

def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show: #verdadeiro
            print(c, end='')
            if c>1:
                print(f'{c} x ', end='')
            else:
                print(' =', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, show=True))