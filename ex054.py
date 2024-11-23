from datetime import date
atual = date.today().year
maior = menor = 0
for p in range(1, 8):
    nasc = int(input(f'Em que ano a {p}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'São {maior} pessoas maiores de idade e {menor} menores de idade!')
