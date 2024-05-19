n1 = int(input('Digite o primeiro número: \n'))
n2 = int(input('Digite o segundo valor: \n'))
n3 = int(input('Digite o terceiro valor: \n'))
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
else:
    print('os valores são iguais')
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')