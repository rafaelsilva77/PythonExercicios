n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4]Novos números
    [5]Sair do programa''')
    opcao = int(input('Qual é a sua opçao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é  {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação de {} x {} é  {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print('Entre {} e {} o {} é maior'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre!')
