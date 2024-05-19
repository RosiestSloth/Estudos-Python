import random
numero = 0
usuario = 0
jogo = 0
pi = 0

print('Seja bem vindo ao jogo de par ou impar.')
while True:

    print('Digite um número: ')
    usuario = int(input())
    numero = random.randint(1, 100)
    jogo = numero + usuario
    pi = jogo % 2

    if pi == 0:
        print(f'O resultado é {jogo}')
        print('O número é par.')

    else:
        print(f'O resultado é {jogo}')
        print('O número é impar.')

    print('Você quer continuar? Digite 1 para SIM e 2 para NÃO')
    r = str(input())
    if r == '2':
        break

    elif r == '1':
        print('OK, vamos jogar denovo.')

print('Foi um prazer jogar com você.')