from datetime import date
ano = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digite seu sexo [F/M]:')).upper().strip()
ano_atual = date.today().year
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))
if sexo == 'F':
    print('Você não precisa fazer o alistamento obrigatório!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano_atual + saldo))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano_atual - saldo))


