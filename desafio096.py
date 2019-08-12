# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(base, altura):
    a = base * altura
    print(f'A área de um terreno {base}x{altura} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos ')
print('-' * 20)
ba = float(input('Largura (m): '))
al = float(input('Altura (m): '))
area(ba, al)
