'''n = 0 #aqui eu não disse quantas vezes ele tem q perguntar o nº, não usei um contador
# ele vai me pedir p/ digitar o número infinitamente, só para qundo eu digitar 999
while n != 999: #enquanto não digitar 999 ele roda o loop
    n = int(input('Digite um número: '))'''

'''n = cont = 0 #meu contador começa em 0 e vai perguntar até 3 números e parar
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''

'''n = s = 0 #inicializo a variavel s de soma
while n != 999:
    n = int(input('Digite um número: '))
    s += n #quero somar os valores q eu digitar no programa
print(f'A soma vale {s}')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: #uso o break se o nº for 999
        break #qndo uso o comando break ele sai de um enquanto,
    s += n #ai mostra a soma sem somar 999,a soma só ocorre se o nº não for 999
print(f'A soma vale {s}')
