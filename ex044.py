produto = float(input('Digite o valor do produto: R$'))
print('''
[ 1 ] DINHEIRO/CHEQUE
[ 2 ] CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    desc = produto - (produto * 10 / 100)
    print(f'O valor do produto é R$\033[1;31m{produto:.2f}\033[m e com o desconto de 10% à vista passa a ser '
          f'R$\033[1;32m{desc:.2f}\033[m')
elif opcao == 2:
    desc = produto - (produto * 5 / 100)
    print(f'O valor do produto é R${produto:.2f} e com o desconto de 5% à vista no cartão passa a ser R${desc:.2f}')
elif opcao == 3:
    parc = produto / 2
    print(f'O produto com o valor de R${produto:.2f} será dividido em 2x no cartão, pagando parcelas de R${parc:.2f}')
elif opcao == 4:
    vezes = int(input('Digite em quantas vezes vai passar no cartão: '))
    aumento = produto + (produto * 20 / 100)
    parc = aumento / vezes
    print(f'Passando {vezes}x no cartão seu produto ficará com um total de R${aumento:.2f} e você '
          f'pagará R${parc:.2f} de parcelas')
else:
    print('Opção inválida.')
