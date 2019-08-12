print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50 #começa c/cedula de maior valor
totced = 0 #crio o total de cedulas
while True: #enquanto for verdade faça o loop infinito, q é quebrado qndo acabar o dinhero
    if total >= ced: #se total atual for >= cedulas>
        total -= ced #eu tiro do total o valor dessa cédula, tento tira 50 desse valor
        #qntas vezes der p/ tirar 50 desse valor ele vai subtraindo.
        totced += 1 #a cda vez q eu tirar 50 o meu total d cedulas sera totced += 1
        #c/ esse codigo eu vejo qntas vezes eu posso tirar 50, se não der p/ tirar ai verifico qual a cedula atual
    else:
        if totced > 0: #se totced for >0 ele printa, assim se uma ced nao for usada ela nao é printada
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50: #se ced atual é 50 significa q nao consegui mais tirar 50 do valor
            ced = 20 #entao a prox ced é de 20.
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0 #cda vez q mudo a nota tem q fzer o totdecedulas voltar a 0.
        if total == 0: #isso vai parar se total for = 0
            break
print('=' * 30)
print('Volte sempre ao Banco CEV.')
