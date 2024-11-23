peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura**2)
print(f'O seu imc é {imc:.1f} então você está ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('no PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESO')
else:
    print('com OBESIDADE MÓRBIDA')
