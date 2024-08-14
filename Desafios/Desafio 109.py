#Importa o Módulo moeda da pasta Módulos
from Modulos import moeda

#Recebe o valor digitado pelo usuário e armazena na variável num
num = float(input('Digite um valor: R$'))

#Recebe os parâmetros do módulo

#aqui Recebe o valor da moeda formatado em BRT R$00,0
Preco = moeda.moeda(num)

#Separa os requisitos de metade dobro e soma
metade = moeda.moedas_metade(num, format=True)
dobro = moeda.moedas_dobro(num, True)
aument = moeda.moedas_aumentar(num, 10, format=True)
dimin = moeda.moedas_diminuir(num, 20, True)

#Imprime para o usuário os valores
print(f'A medade de {(Preco)} é {(metade)}')
print(f'O dobro de {(Preco)} é {(dobro)}')
print(f'Aumentando 10%, temos {(aument)}')
print(f'Diminuindo 20% temos: {(dimin)}')