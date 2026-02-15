def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.2f}m²')

print(' Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('CONPRIMENTO (m): '))
área(l, c)