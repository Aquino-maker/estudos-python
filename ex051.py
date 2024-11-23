print('-=' * 15)
print(f'{'10 TERMOS DE UMA P.A':^30}')
print('-=' * 15)
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for i in range(t, d, r):
    print(f'{i}', end=' -> ')
print('FIM')