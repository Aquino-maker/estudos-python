import math
a = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print(f'O seu ângulo é {a}º \nSeno de {a} = {sen:.1f}')
print(f'Cosseno de {a}º = {cos:.1f}')
print(f'Tângente de {a}º = {tg:.1f}')