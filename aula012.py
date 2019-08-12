def analisador_nome(nomes):
    if nome == 'Gustavo':
        print('Nome lindo')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Nome popular')
    elif nome in 'Ana Cláudia Jéssica Juliana':
        print('nome feminino bonito')
    else:
        print('nome normal')
    return nomes

nome = input('Seu nome: ')
analise = print(analisador_nome(nome))



#ex de estrutura condicional aninhada
"""nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))"""
