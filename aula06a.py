def soma(n1, n2):
    """Função que retorna a soma de n1 e n2"""
    s = n1 + n2
    return s

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma entre', n1, 'e', n2, 'vale', soma(n1, n2), '.')
