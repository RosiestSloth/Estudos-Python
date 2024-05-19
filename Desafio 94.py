from time import sleep

pessoas = []
count = 0
soma_idades = 0
mulheres = 0

print('Seja bem vindo ao nosso programa de cadastramento de pessoas\n', '-=' * 30)
print('Iniciando...')
sleep(2)

while True:
    pessoa = {}
    pessoa['Nome'] = str(input('Digite o nome: '))
    pessoa['Idade'] = int(input('Digite a idade: '))
    pessoa['Sexo'] = str(input('Digite o sexo (M/F): ')).upper()

    count += 1
    pessoas.append(pessoa)

    resp = str(input('Você quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

print(f'O grupo tem {count} pessoas')

for c in range(count):
    for k, v in pessoas[c].items():
        print(f'{k.upper()}\n{v}')
        if k == 'Idade':
            soma_idades += v
        elif k == 'Sexo' and v == 'F':
            mulheres += 1
        print('-='*10)

media_idade = soma_idades / count
print(f'A média de idade do grupo é {media_idade:.2f}')
print(f'A quantidade de mulheres cadastradas é {mulheres}')
