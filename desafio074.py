# programa q vai gerar 5 nºs aleatorios e colocar em uma tupla. Dpois disso, mostre a listagem de nºs gerados e tbm
# indique o menor e o maior valor q estão na tupla.

from random import randint

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
""" OU
n = [randint(1,10) for numero in range(0, 5)]
n = tuple(n)
"""
print(f'Valores sorteados: {n}')
print(f'O maior valor sorteado foi {max(n)} e o menor foi {min(n)}')