def avaliador_nomes(nome):
    if nome == 'Gustavo':
        avaliacao = 'lindo nome'
    else:
        avaliacao = 'nome normal'
    return avaliacao

nome = input('Seu nome: ')
avaliacao = avaliador_nomes(nome)
print(avaliacao)

"""nome = str(input('Qual e o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo.')
else:
    print('Seu nome é normal.')
print('Bom dia {}.'.format(nome))"""