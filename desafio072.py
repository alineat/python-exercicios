# programa q tenha uma tupla totalmente preenchida c/ uma contagem por exrenso, de zero a 20. o rpograma deve ler um nº
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
        "treze", "catorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um nº [0-20]: "))
    if 0 <= num <= 20:
        break
    print("Tete novamente.", end="")
print(f"Você digitou o número {cont[num]}")
"""

cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
        "treze", "catorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")
jogar = "S"
while jogar == "S":
    num = int(input("Digite um nº [0-20]: "))
    while num not in tuple(range(0, 21)):
        num = int(input("valor invalido, digite novamente: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {cont[num]}")
    jogar = input("continuar? ").strip().upper()[0]



