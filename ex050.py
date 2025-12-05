n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite mais um outro valor: '))
n5 = int(input('Digite mais um outro valor: '))
n6 = int(input('Digite o ultimo valor: '))
cont = 0
soma = 0
for c in [ n1, n2, n3, n4, n5, n6 ]:
    if c % 2 == 0:
        cont = cont + 1
        soma += c
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))










'''
soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0:
    soma += num
    cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))'''

