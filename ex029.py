v = int(input('Qual é a velocidade atual do carro?' ))
m = (v - 80) * 7
if m > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R$ {:.2f} '.format(m))
print('Tenha um bom dia! Dirija com cuidado!')