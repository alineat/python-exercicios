# programa q tenha uma tupla c/ várias palavras (ñ usar acentos). dpois disso, vc deve mostrar, p/ cda palavra, quais
# são as suas vogais.

tupla = ("marcenaria", "joalheria", "costura", "pintura")

for palavra in tupla:
    print(f"\nNa palavra {palavra.upper()} temos ", end="")
    for letra in palavra:
        if letra.lower() in "aeiouáâãà":
            print(letra, end=" ")