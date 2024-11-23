a = float(input('Digite a altura em metros: '))
b = float(input('Digite a largura em metros: '))
area = a * b
print(f'A altura de {a}m e a largura de {b}m é igual a uma área de {area}m²')
tinta = area / 2
print(f'Para pintar uma parede \033[1;32m{area}\033[mm² precisará de \033[1;34m{tinta}\033[ml de tinta!')
