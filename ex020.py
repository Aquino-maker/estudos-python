from random import shuffle
n1 = str(input('1º Aluno: '))
n2 = str(input('2º Aluno: '))
n3 = str(input('3º Aluno: '))
n4 = str(input('4º Aluno: '))
itens = [n1, n2, n3, n4]
shuffle(itens)
print(f'A ordem dos alunos é: {itens}')