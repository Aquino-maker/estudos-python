while True:
    n = int(input('Digite o número que quer ver a tabuada: '))
    print('-' * 30)
    if n < 0:
        print('Número inválido, finalizando...')
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c:2}')
    print('-' * 30)
