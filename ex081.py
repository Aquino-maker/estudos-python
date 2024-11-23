valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} elementos!')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valores}')
if 5 in valores:
    print('O Valor 5 está na lista!')
else:
    print('O 5 não está na lista!')
