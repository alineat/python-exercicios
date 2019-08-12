def imc(peso, altura):
    imc_calculo = peso / (altura ** 2)
    print('O IMC dessa pessoa é de {:.2f}'.format(imc_calculo))
    if imc_calculo < 18.5:
        print('Abaixo do peso.')
    elif imc_calculo >= 18.5 and imc_calculo < 25: #da para usar assim 18.5 <= imc < 25:
        print('Peso ideal.')
    elif 25 <= imc_calculo < 30:
        print('Sobrepeso.')
    elif 30 <= imc_calculo < 40:
        print('Obesidade.')
    elif imc_calculo >= 40:
        print('Obesidade mórbida.')
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc(peso, altura)
