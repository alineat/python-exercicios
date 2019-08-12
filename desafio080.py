# usuário digita 5 valores numéricos e cadastra em uma lista, já na posição correta de inserção (sem usar o sort()).
# No fim, mostra a lista ordenada na tela.

lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("adicionado ao final da lista")
    else:
        pos = 0 #posição-pos
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print("adicionado na posição {pos}")
                break
            pos += 1

print(f"Os números digigtados foram: {lista}")