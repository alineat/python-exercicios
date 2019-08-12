# Faça um programa que leia nome e peso de várias pessoasm guardando tudo em uma lista. No final, mostre: a) Quantas
# pessoas foram cadastradas. b) Uma listagem com as pessoas mais pesadas. c) Uma listagem com as pessoas mais leves.

temporary_list = []
principal_list = []
mai = men = 0

while True:
    temporary_list.append(str(input("Nome: ")))
    temporary_list.append(float(input("Peso: ")))
    if len(principal_list) == 0:
        mai = men = temporary_list[1]
        print(mai)
    else:
        if temporary_list[1] > mai:
            mai = temporary_list[1]
        elif temporary_list[1] < men:
            men = temporary_list[1]

    principal_list.append(temporary_list[:])
    print(principal_list)
    temporary_list.clear()
    resp = str(input("Quer continuar [s/n]: "))
    if resp in "nN":
        break
print("-"*30)
print(f"Os dados foram: {principal_list}")
print(f"Ao todo foram cadastradas {len(principal_list)} pessoas.")
print(f"O maior peso foi de {mai} Kg. Peso de ",end="")
for pessoa in principal_list:
    if pessoa[1] == mai:
        print(f"[{pessoa[0]}]", end=" ")
print()
print(f"O menor peso foi de {men} Kg. Peso de ", end="")
for pessoa in principal_list:
    if pessoa[1] == men:
        print(f"[{pessoa[0]}]",end=" ")
print()
