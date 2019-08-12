"""
# 1
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma de {} + {} é {}.'.format(n1, n2, soma))

"""
"""
# 2
variavel = " k"
print(variavel.isspace())
"""
"""
# 3- analisando um texto
nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome têm {len(nome) - nome.count(' ')} letras.") #count subtrai os espaços em branco encontrados. Ex de comentario inline, ñ é recomendado em python

dividido = nome.split(" ")
print(f"O seu primeiro nome têm {len(dividido[0])}")
"""
"""
# 4- Separando digitos de um numero #faça loop dpois
num = int(input("Informe um número: "))
n = str(num)
print(f"Unidade: {n[3]}")
print(f"Dezena: {n[2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")
"""
"""
# 5- Primeiras letras de um texto - leia o nome da cidade e diga se ela começa ou não com "Santo"
nome = str(input("Nome da cidade: ")).strip().upper()
separe = nome.split()
print(f"A cidade {nome} começa com o nome 'Santo'? {'SANTO'==separe[0]}")
"""
"""
# 6- Procurando uma string dentro de outra string - leia nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input("Nome completo: ")).strip().upper().split()
print(f"Seu nome tem 'Silva'? {'SILVA' in nome}")
"""
"""
# 7- Primeira e última ocorrência dentro de um texto - leia uma frase e mostre qntas vezes aparece a letra "a", em q
# posição ela aparece pela 1ª vez e em q posição aparece pela última vez
frase = str(input("Escreva a sua frase: ")).strip().upper()
print(f"A letra 'a' aparece: {frase.count('A')} vez(es)\nAparece pela primeira vez na posição {frase.find('A')+1}\ne 
pela última vez na posição {frase.rfind('A')+1}")
"""
"""
# 8- Primeiro e último nome - leia o nome completo e mostre o primeiro e ultimo nome separadamente
nome = str(input("Nome completo: ")).strip().upper().split()
print(f"Primeiro nome: {nome[0]}\nÚltimo nome: {nome[-1]}") #OU
print(f"Primeiro nome: {nome[0]}\nÚltimo nome: {nome[len(nome)-1]}")
"""
"""
# 9- Dicionário de cores escape sequence
estilo = {"none": "\033[0m",
          "bold": "\033[1m",
          "underline": "\033[4m",
          "negative": "\033[7m",
          "limpa": "\033[m"}
texto = {"branco": "\033[30m",
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
        "azul": "\033[34m",
        "violeta": "\033[35m",
        "turqueza": "\033[36m",
        "cinza": "\033[37m"}
back = {"branco": "\033[40m",
        "vermelho": "\033[41m",
        "verde": "\033[42m",
        "amarelo": "\033[43m",
        "azul": "\033[44m",
        "violeta": "\033[45m",
        "turqueza": "\033[46m",
        "cinza": "\033[47m"}
print(f"{estilo['negative']}estilo {estilo['limpa']}")
print(f"{texto['turqueza']}texto{estilo['limpa']}")
print(f"{back['vermelho']}background vermelho{estilo['limpa']}.")
"""
"""
#peça um valor p/ o usuario 4 vezes e some esses valores no final
s = 0
c = 0
for c in range(0, 4):
    n = int(input("Digite um nº: "))
    s = s + n
    c = c + 1
print(f"O somatório dos {c} valores foi {s}")
"""
"""
soma = cont = 0
for c in range(1,5):
    cont = cont + 1
    print(f"Contagem: {cont-1} + 1 = {cont}")
    soma = soma + c
    print(f"Somatório: {soma} + {c} = {soma}\n") #ta errado só o print da primeira soma,ainda nao sei como imprimir certo
"""
"""
a=True
b=True
c=True
d=False

def follows(a,b):
    return not a or b

print('oi')
climate_change = follows(follows(a,b),c)
print(climate_change)
if not d:
    print(climate_change)
else:
    print(d)
"""
"""
way = 2.7
sti = 2.3
_var = 2.3
smeeee = 1.3

a = way > sti
b = sti < smeeee and a
c = _var >= sti
c = a and b or c and smeeee > 1.2
d = not ((a and b) or c)
print(a, b, c, c, d)
if c and a:
    print(d)
    print('oi')
else:
    print(not d)
    print('ola')
"""
"""
gatos = {'ingles': 'cat', 'espanhol': 'gato', 'frances': 'chat'}
gatos['portugues'] = 'gato'
print(gatos)
gatos.update({'alemão': 'katze', 'italiano': 'gatto'})
print(gatos)
del gatos['ingles']
gatos.pop('espanhol')
print(gatos)
print(gatos.get('russo', 'desconhecido'))
"""
"""
lanches = ('banana', 'maçã', 'melão')
for comida in lanches:
    if comida in lanches[-1]:
        print(comida, end=".")
    else:
        print(comida, end=", ")
"""
