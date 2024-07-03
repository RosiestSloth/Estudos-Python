from Modulos import moeda

num = float(input('Digite um valor: R$'))

print(f'A medade de {num:.2f} é R${moeda.moedas_metade(num):.2f}')
print(f'O dobro de {num:.2f} é {moeda.moedas_dobro(num):.2f}')
print(f'Aumentando 10%, temos R${moeda.moedas_aumentar(num, 10):.2f}')