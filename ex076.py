produtos = ('Laptop', 3000,
            'Cadeira Gamer', 800,
            'Monitor 24"', 1200,
            'Teclado Mecânico', 350,
            'Mouse Óptico', 150,
            'Headset', 250,
            'Webcam HD', 200,
            'Impressora Multifuncional', 600,
            'Mesa de Escritório', 900,
            'Cabo HDMI', 50)
print('-=' * 15)
print(f'{'TABELA DE PREÇOS':^30}')
print('-=' * 15)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
