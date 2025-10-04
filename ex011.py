l = float(input('Largura da parede:'))
a = float(input('Altura da parede: '))
area = l * a
p = area / 2
print('Sua parede tem a dimenção de {}x{}  e sua área é de {:.1f}m²'.format(l, a, area))
print('Pra pintar essa parede, você precisará de {:.1f}l de tinta'.format(p))