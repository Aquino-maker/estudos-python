mais18 = totH = mulher20 = 0
while True:
    print('=' * 30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('=' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você registou {mais18} com mais de 18 anos.')
print(f'{totH} homens foram registrados!')
print(f'E temos {mulher20} mulheres com menos de 20 anos!')
