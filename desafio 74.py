import random
numero = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
           random.randint(1, 100), random.randint(1, 100))
print(numero)
menor = min(numero)
maior = max(numero)
print(f'o menor número é {menor}, e o maior número é {maior}')