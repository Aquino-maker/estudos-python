from random import randint
palpite = 0
computador = randint(1, 10)
print('[COMPUTADOR] - Pensei em um número consegue adivinhar qual foi? Vamos tente!')
while True:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador != computador:
        print('Você errou, tente mais uma vez... ', end='')
        if jogador > computador:
            print('Só que dessa vez um número mais abaixo')
        else:
            print('Só que dessa vez um número mais alto.')
    else:
        break
print(f'Você fez {palpite} palpites para acertar o número, meus parabéns!')
