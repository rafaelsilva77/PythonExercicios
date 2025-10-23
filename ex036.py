vcasa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
prestaçãomensal = (vcasa / financiamento) / 12
if salário > prestaçãomensal * 30 / 100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \n Empréstimo NEGADO!'.format(vcasa, financiamento, prestaçãomensal))
else:
    print('Para pagar R${:.2f} em {} anos será de R${:.2f} \n Empréstimo pode ser CONCEDIDO!'.format(vcasa, financiamento, prestaçãomensal))