km = float(input('Quantos KM foram percorridos? '))
dias = int(input('Quantos dias de uso? '))
alugel = (km * 0.15) + (dias * 60)
print(f'Analisando todos os dados, você deve pegar R${alugel:.2f} pelo carro alugado!')