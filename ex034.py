salário = float(input('Qual é o salário do funcionário? '))
aumento1 = salário + (salário * 10 / 100)
aumento2 = salário + (salário * 15 / 100)
if salário > 1250:
    print('Quem ganhava \033[31mR${:.2f}\033[m passa a ganhar \033[32mR${:.2f}\033[m agora'.format(salário,aumento1))
else:
    print('Quem ganhava \033[31mR${:.2f}\033[m passa a ganhar \033[32mR${:.2f}\033[m agora'.format(salário,aumento2))