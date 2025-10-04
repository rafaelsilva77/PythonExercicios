d = float(input('Quantos dias alugados? '))
r = float(input('Quantos Km rodados? '))
cd = 60 * d
cr = cd * 0.15
ct = cr + cd
print('O total a pagar é de R${:.2f}'.format(ct))