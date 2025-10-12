from time import sleep
num = int(input('Informe um número: '))
u = num // 1 % 10000
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[34mAnalisando o número {} ...\033[m'.format(num))
sleep(3)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))