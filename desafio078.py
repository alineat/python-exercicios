# programa q leia 5 valores numéricos e guarde-os em uma lista. Mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista
"""
#solucao incompleta, para fzer um loop q qndo houver mais de um numero igual imprima tdas as posições
lista = []
cont = 0
for numero in range(0,5):
    numeros = int(input(f"Digite o {cont+1}º número: "))
    cont += 1
    lista.append(numeros)
print(lista)
print(f"Maior nº: {max(lista)}, está na posição {lista.index(max(lista))+1}")
print(f"Menor nº: {min(lista)}, está na posição {lista.index(min(lista))+1}")
"""
# Ou, solução do Guanabara

lista = []
maior = menor = 0
for numero in range(0,5):
    numeros = lista.append(int(input(f"Digite o {numero+1}º número: ")))
    if numero == 0:
        maior = menor = lista[numero]
    else:
        if lista[numero] > maior:
            maior = lista[numero]
        if lista[numero] < menor:
            menor = lista[numero]

print(lista)
print(f"Maior nº: {maior}, está nas posições ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end="")

print(f"Menor nº: {menor}, está na posição ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
