while True:     # Começando com um LOOP infinito, enquanto for verdadeiro.
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':      # Verificando se a pessoa digitou 'M' ou 'F'
        print('Inválido, tente novamente.')
    else:
        break   # Quebra do Loop, assim seguindo as proximas funções tranquilamente, logo após obter resposta correta
print(f'Sexo {sexo} registrado com sucesso, obrigado!')
