valores = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
print('-=' * 20)
print(f'Os números pares foram {sorted(valores[0])}')
print(f'Os números impares foram {sorted(valores[1])}')