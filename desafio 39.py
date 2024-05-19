idade = int(input('digite sua idade:'))
if idade < 18:
    print('você ainda não tem idade suficiente para se alistar.')
    print(f'Ainda faltam {18 - idade} anos para se alistar.')
elif idade <= 19:
    print('você já pode se alistar.')
elif idade >= 20:
    print('Já passou o tempo de se alistar.')
    print
else:
    print('digite uma idade válida.')