distancia = float(input('Digite a quantidade de KM da viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'A sua viagem de {distancia}KM ficará por R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'A sua viagem de {distancia}KM ficará por R${preco:.2f}')
