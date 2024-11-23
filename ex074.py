from random import randint
valores = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10),)
print(f'Os valores gerados foram ', end='' )
for n in valores:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(valores)}')
print(f'O menor valor foi {min(valores)}')
