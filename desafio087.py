# Aprimore o desafio anterior, mostrando no final: a) a soma de todos os valores pares digitados. b) a soma dos valores
# da terceira coluna. c) o maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))
print("-"*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]: ^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print()

print("-"*30)
print(f"Lista: {matriz}")
print(f"A soma dos valores pares é: {somapares}")
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f"A soma dos valores da terceira cluna é {somacoluna}.")
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha: {maior}")