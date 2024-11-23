valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=' * 30)
print(f'Foram digitados {sorted(valores)}')
print(f'Os valores pares digitados foram {sorted(par)}')
print(f'Os valores impares digitados foram {sorted(impar)}')