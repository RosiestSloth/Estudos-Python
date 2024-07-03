from Modulos import moeda

num = float(input('Digite um valor: R$'))

metade = moeda.moedas_metade(num)
dobro = moeda.moedas_dobro(num)
aument = moeda.moedas_aumentar(num, 10)

print(f'A medade de {moeda.moeda(num)} é {moeda.moeda(metade)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(dobro)}')
print(f'Aumentando 10%, temos {moeda.moeda(aument)}')