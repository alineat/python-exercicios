s = cont = 0
while True:
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
print(f'Foram digitados {cont} nºs e a soma entre eles é {s}.')