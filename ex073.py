time = ('Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians', 'Fluminense',
        'Internacional', 'Fortaleza', 'Athletico-PR', 'São Paulo', 'Botafogo',
        'Chapecoense', 'Cuiabá', 'Goiás', 'Bahia', 'Vasco', 'Santos', 'Grêmio',
        'Cruzeiro', 'Coritiba', 'Bragantino')
print(f'Os primeiros 5 times são {time[:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são {time[-4:]}')
print('-=' * 15)
print(f'Em ordem alfabetica: \n{sorted(time)}')
print('-=' * 15)
print(f'Chapecoense se encontra na {time.index("Chapecoense")+1}ª posição')
