valores = []
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Esse valor já foi adicionado, então não será adicionado novamente.')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
