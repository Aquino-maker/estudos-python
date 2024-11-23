total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} itens acima ou igual à R$1000.00 reais.')
print(f'O produto mais barato foi \033[1;33m{barato}\033[m que custa R${menor:.2f}')
