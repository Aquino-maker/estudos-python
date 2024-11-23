from time import sleep


def maior(* num):
    cont = mai = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\tForam informados {cont} valores ao todo.')
    sleep(0.2)
    print(f'O maior valor é {mai}')


# Programa principal
maior(2, 9, 4, 5, 7, 11)
maior(4, 7, 0, 1)
maior(1, 2)
maior(6)
maior()
