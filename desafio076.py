# programa q tenha uma tupla única c/ nomes de produtos e seus respectivos preços, na sequencia. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

tupla = ("manga", 2, "banana", 5, "café", 8.99, "pera", 1.2, "melancia", 25, "leite", 2.75, "pêssego", 10,
         "nectarina", 12, "pinha", 2)
print("-"*10, "Listagem de preços", "-"*10, "\n")

for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f"{tupla[posicao]:.<30}", end="")
    else:
        print(f"R${tupla[posicao]:>7.2f}")