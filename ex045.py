from time import sleep
from random import randint
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('[COMPUTADOR]: Olá humano, veio me desafiar a um jokenpô? Então vamos!')
print('''Escolha sua jogada 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 20)
print(f'Computador escolheu {itens[computador]}')
print(f'Jogador escolheu {itens[jogador]}')
print('-=' * 20)
print('Calculando resultado...')
sleep(0.3)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Jogada inválida.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida')