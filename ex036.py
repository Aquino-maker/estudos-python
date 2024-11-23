casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto é seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
maximo = salario * 30 / 100
print(f'Para pagar uma casa com o valor de R${casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R${prestacao:.2f}')
if prestacao <= maximo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
