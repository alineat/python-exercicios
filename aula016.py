#Usando o for em tuplas:
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in lanche:
    print(c)
print('-*' * 11)

#OU, se eu precisar da posição do elemento

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')
print('-*' * 11)

for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')
print('-*' * 11)

