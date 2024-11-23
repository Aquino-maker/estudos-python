print('-=' * 15)
print(f'{'GERADOR DE P.A':^30}')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}', end=' -> ')
        termo += razao
        c += 1
    print('FIM')
    mais = int(input('Quantos termos você quer a mais? '))
print(f'Progressão realizada com sucesso com {total} termos mostrados!')
