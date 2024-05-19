idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
else:
    print('Digite um número válido.')