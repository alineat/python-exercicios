# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
#  conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input(f'Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('-'*30)
for key, value in aluno.items(): #p/ cda chave e valor em aluno.items
    print(f'{key} é igual a {value}')