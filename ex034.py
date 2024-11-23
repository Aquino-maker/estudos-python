sal = float(input('Digite o salário: '))
if sal <= 1250:
    aumento = sal + (sal * 15 / 100)
    print(f'O salário do funcionário que era \033[1;31mR${sal:.2f}\033[m aumentou para \033[1;32mR${aumento:.2f}\033[m')
else:
    aumento = sal + (sal * 10 / 100)
    print(f'O salário do funcionário que era \033[1;31mR${sal:.2f}\033[m aumentou para \033[1;32mR${aumento:.2f}\033[m')

