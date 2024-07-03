nome = str(input('Digite seu nome completo: '))

print('Analisando nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')

separa = nome.split()

print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')