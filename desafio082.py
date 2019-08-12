# leia variso nºs e coloque-os em uma lista. Dpois, crie duas listas extras q vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao fim, mostre o conteúdo das três listas geradas.

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("Digite um nº: ")))
    resp = str(input("Quer continuar? "))
    if resp in "nN":
        break
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f"A lista completa é {num}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")
