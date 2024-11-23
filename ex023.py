from time import sleep
num = int(input('Digite um número inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número...')
sleep(1)
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c} \nMilhar: {m}')