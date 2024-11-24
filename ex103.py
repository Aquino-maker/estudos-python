def ficha(jogador, gol):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Números de gol: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(jogador='Desconhecido', gol=g)
else:
    ficha(n, g)
