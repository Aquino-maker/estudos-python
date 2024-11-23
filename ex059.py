from time import sleep
n1 = int(input('1º Valor: '))
n2 = int(input('2º Valor: '))
while True:
    print(f'''{' OPÇÕES ':=^30}
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>Qual opção deseja? '))
    match opcao:
        case 1:
            print(f'\n{n1} + {n2} = {n1 + n2}\n')
        case 2:
            print(f'\n{n1} x {n2} = {n1 * n2}\n')
        case 3:
            if n1 > n2:
                print(f'\n{n1} é o maior valor!\n')
            else:
                print(f'\n{n2} é o maior valor!\n')
        case 4:
            n1 = int(input('\nNovo 1º valor: '))
            n2 = int(input('Novo 2º valor: '))
        case 5:
            print('Finalizando...')
            sleep(1)
            break
print('Obrigado por utilizar o programa.')
