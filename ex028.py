from random import randint
computador = randint(0, 5)
tent = int(input('Computador: Eu pensei em um número, consegue adivinhar qual? \n'))
print(f'Computador: O número que eu pensei foi: \033[1;33m{computador}\033[m \nlogo você ', end='')
if tent == computador:
    print('\033[1;32mACERTOU!!\033[m')
else:
    print('\033[1;31mERROU!!\033[m')
