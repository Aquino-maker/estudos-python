from datetime import date
atual = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = atual - ano
if idade == 18:
    print(f'Como nascido em {ano} você tem {idade} logo deve se alistar, imediatamente!!')
elif idade > 18:
    saldo = idade - 18
    print(f'Nascido em {ano} você deveria ter se alistado a {saldo} anos atrás.')
else:
    saldo = 18 - idade
    print(f'Nascido em {ano} você ainda deve esperar {saldo} para se alistar.')