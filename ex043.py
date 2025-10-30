peso = float(input('Qual é o seu peso? (kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25: #  18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc >= 25 and imc < 30:   # 25 <= imc < 30:
    print('Você está com EXCESSO DE PESO')
elif imc >= 30 and imc < 40:  # 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está com OBESIDADE MORBIDA, cuidado!')