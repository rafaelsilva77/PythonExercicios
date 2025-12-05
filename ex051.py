primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo + razão,razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')




'''
print('= ' * 40)
print('        10 TERMOS DE UMA PA')
print('=' * 40)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

for c in range(termo,razao * 10,razao):
    print(c, end=' -> ')
print('Acabou')'''
