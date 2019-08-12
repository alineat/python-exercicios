num = cont = soma = 0 #usa uma linha p/ atribuir todas as variáveis
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitoy {} números e a soma entre eles foi {}.'.format(cont, soma))
