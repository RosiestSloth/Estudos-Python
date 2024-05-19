n = 0
while True:
    n = int(input('Digite um número para o jogo: '))
    if n < 10:
        print('Digite um número maior.')
    elif n > 10:
        print('Digite um número menor.')
    if n == 10:
        break
print('Você conseguiu. Parabéns.')