print('=' * 30)
print(f'{'BANCO AQUINO':^30}')
print('=' * 30)
valor = int(input('Digite o valor a ser sacada: R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Foram retiradas {totced} de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 30)
print('Obrigado por utilizar o sistema do BANCO AQUINO')