print('=-' * 6, '10 termos de uma PA', '-=' * 6)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais #(total é 0 + qntos termos ele quer mostrar)
    while cont <= total: #nao posso mais usar 10 pq o usuario pode digitar outro valor
        print(f'{termo} ->', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você mostrar a mais? '))
print('Processo finalizado, com {} termos mostrados.'.format(total))