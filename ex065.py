soma = maior = menor = qnt = 0
while True:
    n = int(input('Digite um valor: '))
    qnt += 1
    soma += n
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp in 'Nn':
        break
media = soma / qnt
print(f'Você digitou {qnt} números e a média deles é {media}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
