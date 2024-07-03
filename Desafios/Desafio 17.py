import math

opo = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))

hip = math.hypot(adj, opo)

print(f'A hypotenusa dos valores inseridos é de {hip:.2f}')