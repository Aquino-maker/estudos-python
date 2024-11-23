from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in dados.items():
    print(f'    {k} tirou {v} no dado')
    sleep(0.7)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 3, f'{'RANKING'}', '-=' * 3)
for i, v in enumerate(ranking):
    print(f'    - {i+1}º lugar: {v[0]} com {v[1]} no dado')
    sleep(0.7)
