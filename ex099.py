from time import sleep

def  maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')



maior(9, 4, 3, 2, 11, 0)
#maior(7, 3, 5, 6)
#maior(5, 3)
#maior(0)