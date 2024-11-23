valores = (int(input('Digite um valor: ')), int(input('Digite mais um valor: ')),
           int(input('Digite outro valor: ')), int(input('Digite o ultimo valor: ')))
print(f'\nVocê digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n} ', end='')