pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram registradas {len(pessoas)} pessoas')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(p[0])
print(f'O menor peso foi {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0])
