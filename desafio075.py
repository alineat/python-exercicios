# desenvolva um programa q leia 4 valores pelo teclado e guarde-os em uma tupla. no final, mostre: a)qntas vezes
# apareceu o valor 9; b) em q posição foi digitado o primeiro valor 3. c) quais foram os primeiros pares.
# P.S: MINHA SOLUÇÃO MELHORADA
valores = []
for numero in range(1,5):
    numero = int(input("Digite um nº: "))
    valores.append(numero)
tupla = tuple(valores)
print(tupla)

print(f"O valor 9 apareceu: {tupla.count(9)} vez(es)")
if 3 in tupla:
    print(f"O valor 3 foi digitado 1º na posição {tupla.index(3)}")
else:
    print(f"O valor 3 não foi digitado.")
print(f"Os primeiros pares foram ", end="")
for p in tupla:
    if p % 2 == 0:
        print(p, end=" ")
