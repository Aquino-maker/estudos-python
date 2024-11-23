veloc = int(input('Digite a sua velocidade: '))
if veloc > 80:
    multa = (veloc - 80) * 7
    print(f'A sua velocidade ultrapassou os 80km/h permitidos, isso lhe rende uma multa de R${multa:.2f}')
else:
    print('\033[1;32mA sua velocidade está ótima, continue assim.')
