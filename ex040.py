n1 = float(input('1º Nota: '))
n2 = float(input('2º Nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f} o aluno obtem uma média de {media:.1f}')
if 7 > media >= 5:
    print('\033[1;33mVocê está em recuperação!\033[m')
elif media < 5:
    print('\033[1;31mVocê está REPROVADO\033[m')
else:
    print('\033[1;32mVocê está Aprovado!\033[m')