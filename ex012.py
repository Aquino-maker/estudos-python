preco = float(input('Digite o preço do produto: R$'))
desc = preco - (preco * 5 / 100)
print(f'O seu produto é R${preco} e com o desconto de 5% ficará por R${desc}')
