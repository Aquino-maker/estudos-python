salario = float(input('Digite o salário do funcionario: R$'))
aumento = salario + (salario * 15 / 100)
print(f'O salário do trabalhador era de R$\033[31m{salario:.2f}\033[m ', end='')
print(f'e depois de um aumento de 15% ficou R$\033[1;32m{aumento:.2f}\033[m')
