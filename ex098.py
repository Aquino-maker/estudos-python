from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= 1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.1)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.1)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar!!')
inicio = int(input('Digite um número para iniciar a contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite de quanto em quantos números: '))
contador(inicio, fim, passo)
