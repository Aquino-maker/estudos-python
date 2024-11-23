ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    if media >= 7:
        situacao = 'Aprovado'
    elif 5 <= media < 7:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    ficha.append([nome, [n1, n2], media, situacao])
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N')
    if resp == 'N':
        break
print('-=' * 40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}{"SITUAÇÃO":>15}')
print('-' * 40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}{a[3]:>15}')
while True:
    print('-' * 40)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} foram {ficha[opc][1]}')
print('<<< Obrigado por utilizar >>>')
