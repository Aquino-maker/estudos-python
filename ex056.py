maiorIdadeHomem = mediaIdade = nomeVelho = mulherNova = somaIdade = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    print('-=' * 15)
    somaIdade += idade
    mediaIdade = somaIdade / 4
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherNova += 1
print(f'A média de idade é {mediaIdade} anos, daqueles quais foram registrados!')
print(f'O nome do homem mais velho é {nomeVelho} com a idade de {maiorIdadeHomem} anos.')
print(f'Ao todos são {mulherNova} mulher(es) com menos de 20 ano(s)!')
