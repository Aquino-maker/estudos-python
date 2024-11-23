lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(comida)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('Slk, enchi o bucho.')