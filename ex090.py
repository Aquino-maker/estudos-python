ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input('Media: '))
if ficha['media'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in ficha.items():
    print(f'    - {k} é igual a {v}')
