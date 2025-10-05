from math import sin,cos,tan,radians
angulo = float(input('Digite um angulo: '))
seno =sin(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno =cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente =tan(radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))


'''import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))'''


