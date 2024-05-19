from random import randint
from time import sleep

def sorteia():
    for c in range(5):
        numeros.append(randint(0, 5))

def SomaPar():
    soma = 0
    print('Os valores sorteados foram:')

    for a in numeros:
            print(f'{a}', end=' ')
            
    print('')

    for n in numeros:

        if n%2 == 0:
            print(f'O número {n} é par')
            soma += n
            print(f'Somando...')
            sleep(1)

        else:
            print(f'O número {n} não é par')
            sleep(1)

    if soma <= 0:
        print('O valor foi igual a 0')

    else:
        print(f'A soma dos valores pares foi {soma}')


numeros = []
sorteia()
SomaPar()