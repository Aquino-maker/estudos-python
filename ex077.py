palavras = ('significado', 'perseverança', 'empatia', 'aurelio',
            'amor', 'perspicaz', 'peculiar', 'perspectiva', 'resiliencia',
            'genocida', 'reciprocidade', 'carater', 'diligencia', 'anuencia',
            'dissimulado')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra} ', end='')
