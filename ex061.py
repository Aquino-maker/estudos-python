print('-=' * 15)
print(f'{'GERADOR DE P.A':^30}')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    c += 1
print('FIM')
