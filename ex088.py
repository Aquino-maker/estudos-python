from random import randint
from time import sleep
print('-=' * 15)
print(f'{'JOGOS DA MEGA-SENA':^30}')
print('-=' * 15)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
lista = list()
jogos = list()
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.7)
print('-=' * 3, 'Finalizado', '-=' * 3)
