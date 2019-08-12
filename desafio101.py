# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
''' Minha solução
from datetime import date


def voto(ano_nasc):
    global idade
    idade = date.today().year - ano_nasc
    if idade < 16:
        return "voto Negado"
    elif 16 <= idade <= 18 or idade > 60:
        return "voto opcional"
    else:
        return "voto obrigatório"


ano_nascimento = int(input('Em que ano você nasceu? '))
idade = int()
resultado = voto(ano_nascimento)
print(f'Você tem {idade} anos: {resultado}.')
'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
