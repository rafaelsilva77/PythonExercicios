from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar"
print('\033[34m-=-\033[m' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? ')) # o jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}! '.format(computador, jogador))