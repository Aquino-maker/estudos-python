n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O número é \033[1;32mPAR\033[m')
else:
    print('O número é \033[1;31mIMPAR\033[m')
