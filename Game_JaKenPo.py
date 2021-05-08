from random import choice
from time import sleep
lista = ['Pedra','Papel','Tesoura']
computador = choice(lista)
jogador = int(input('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20)
if jogador == 0:
    if computador == 'Papel':
        print('Computador jogou {}'.format(computador))
        print('Você Perdeu!')
    elif computador == 'Tesoura':
        print('Computador jogou {}'.format(computador))
        print('Você Ganhou!')
    else:
        print('Empate você o computador escolheram {}'.format(computador))
elif jogador == 1:
    if computador == 'Pedra':
        print('Computador jogou {}'.format(computador))
        print('Você ganhou!')
    elif computador == 'Tesoura':
        print('Computador jogou {}'.format(computador))
        print('Voce perdeu!')
    else:
        print('Empate você o computador escolheram {}'.format(computador))
else:
    if computador == 'Papel':
        print('Computador jogou {}'.format(computador))
        print('Voce ganhou!')
    elif computador == 'Pedra':
        print('Computador jogou {}'.format(computador))
        print('Voce perdeu!')
    else:
        print('Empate você o computador escolheram {}'.format(computador))
print('-='*20)
print('Fim de jogo')


