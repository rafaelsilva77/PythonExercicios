tot = totMil = cont = menor = nomePMe = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    tot += preço
    if cont == 1:
        menor = preço
        nomePMe = produto
    elif preço < menor:
        menor = preço
        nomePMe = produto
    if preço > 1000:
        totMil += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totMil} produtos custando mais de R$1000.00')
print(f'O menor produto foi {nomePMe} e ele custa {menor:.2f} reais')