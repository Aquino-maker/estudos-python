n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')