from Modulos import moeda

num = float(input('Digite um valor: R$'))

metade = moeda.moedas_metade(num)
dobro = moeda.moedas_dobro(num)
aument = moeda.moedas_aumentar(num, 10)

print(f'A medade de {(num)} é {(metade)}')
print(f'O dobro de {(num)} é {(dobro)}')
print(f'Aumentando 10%, temos {(aument)}')