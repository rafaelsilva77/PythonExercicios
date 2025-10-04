preço = float(input('Qual o preço do produto? R$'))
desconto = 5
preçocomdesconto = preço - (preço * desconto / 100)
print('O preço que custava  R${}, na promoção com desconto de 5% vai custar R${}. '.format(preço, preçocomdesconto ))