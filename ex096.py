def area(l, c):
    a = larg * comp
    print(f'A área de um terreno {l} x {c} é de {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
larg = float(input('Digite a largura em metros: '))
comp = float(input('Digite o comprimento em metros: '))
area(larg, comp)
