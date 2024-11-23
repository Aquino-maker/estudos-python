a = float(input('1º Segmento: '))
b = float(input('2º Segmento: '))
c = float(input('3º Segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Você pode formar um triângulo!')
else:
    print('Você é incapaz de formar um triângulo com esses segmentos')
