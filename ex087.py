matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = mai = scol = 0
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite um valor para [{linha}, {c}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
        if matriz[linha][c] % 2 == 0:
            par += matriz[linha][c]
    print()
print('-=' * 30)
print(f'A soma dos números pares é {par}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma da 3ª coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'O maior número da segunda linha é {mai}')