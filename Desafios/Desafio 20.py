import random

a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segudo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print(f'A ordem de apresentação será')
print(lista)