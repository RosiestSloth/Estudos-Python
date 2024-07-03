km_rodado = float(input('Digite quandos KM foram rodados pelo carro: '))
dias_alugados = int(input('Digite a quantidade de dias em que foi alugado: '))

km_rodado *= 0.15
dias_alugados *= 60

print(f'O valor por KM rodado ficou em R${km_rodado} e o valor por dias alugados ficou em R${dias_alugados}')
print(f'O total ficou em R${km_rodado + dias_alugados}')