n = int(input('Digite um número inteiro: '))
e = int(input('''Digite o número de acordo com as opções abaixo para converter:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
Digite: '''))
if e == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]}')
elif e == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}')
elif e == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('ESCOLHA INVÁLIDA.')
