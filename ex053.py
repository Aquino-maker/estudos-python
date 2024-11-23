frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'A frase digitada é {junto} e o inverso é {inverso} então ', end='')
if inverso == junto:
    print('TEMOS UM PALÓNDROMO!')
else:
    print('a frase digitada não é um palíndromo')