listagem = ('caneta', 1.75,
            'lápis', 1.25,
            'giz', 2,
            'caderno', 10.50,
            'compasso', 3.75,
            'mochila', 50)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = ' ')
    else:
        print(f'R${listagem[pos]:>4.2f}')
print('-'*40)