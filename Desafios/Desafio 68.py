import random
usuario = 0
maquina = 0
numero = 0
pi = 0
rand = 0
r = 0
resposta = ''
print('Vamos jogar o jogo de Par ou Impar \n Digite um valor superior a 50 para encerrar o rpograma')
while True:
    print('Digite um número de 1 a 50:')
    numero = int(input())
    rand = random.randint(1, 50)
    print('Digite [P] para Par e [I] para Impar')
    pi = input('')
    r = (numero+rand)%2
    print('Digite sua resposta.\n[P] para Par e [I] para Impar.')
    resposta = str(input())
    if r == 0:
        print(f'O número é par. \nSua resposta foi: {resposta}')
        if resposta == 'P':
            print('Está correto.')
            usuario += 1
        elif resposta == 'I':
            print('Sua resposta está errada.')
            maquina += 1
    elif r == 1:
        if resposta == 'I':
            print('Está correto.')
            usuario += 1
        elif resposta == 'P':
            print('Sua resposta está errada.')
            maquina += 1
    end = str(input('Você quer continuar jogando? S/N'.upper))
    while True:
        if end == 'S':
            print('OK. Vamos jogar denovo.')
        elif end == 'N':
            break
print(f'Você fez {usuario} e o computador fez {maquina} pontos. \nObrigado por jogar. Esperamos você novamente.')