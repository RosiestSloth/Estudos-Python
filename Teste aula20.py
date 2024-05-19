#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.items())
#A repetição abaixo irá imprimir nome, sexo e idade e depois irá imprimir os respectivos dados
#for k, v in pessoas.items():
#    print(f'{k} = {v}', f'{"-":^5}')
#    print('-'*28)

#O .values() irá imprimir apenas os valores de suas respectivas chaves ex: 'nome': 'Gustavo'. Irá imprimir Gustavo
#O .keys() é apenas para o nome do produto dentro da variável ex: 'nome': 'Gustavo'. Irá imprimir apenas o nome
#O .items irá imprimir todos os dados como por exemplo: 'nome': 'Gustavo'. Irá imprimir nome e Gustavo

#print(pessoas.values())
#print(pessoas.keys())
#print(pessoas.items())
#print(pessoas)
#del pessoas['sexo']
#print(pessoas)
#pessoas['nome'] = 'Leandro'
#brasil = list()
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado'))