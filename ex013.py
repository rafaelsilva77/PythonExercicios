s = float(input('Qual o salário do funcionário? R$'))
aumento = 15
aumentodesalario = s + (s * aumento/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, aumentodesalario))