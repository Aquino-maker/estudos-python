from random import randint
v = 0
print('[COMPUTADOR]: Eu te desafio a um jogo de PAR ou IMPAR')
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador} o total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você Perdeu.')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {v} vezes consecutivas, meus parabéns!')
