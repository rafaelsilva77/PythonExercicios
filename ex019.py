from random import choice
a1 = str(input('Digite o nome do primeito aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceito aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
r = choice(lista)
print('O aluno escolhido foi {}'.format(r))