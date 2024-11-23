maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso lido foi {menor}Kg')
print(f'Já o maior peso lido foi {maior}Kg')
