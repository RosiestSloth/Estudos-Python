import random
import time

print('\033[1;33m', '-='*20,'\n', '          JOGA NA MEGA SENA\n', '-='*20, '\033[0m')
rep = int(input('Quantos jogos você quer que eu sorteie?\n'))
num = list()

print('-='*20, f'\n           SORTEANDO {rep} JOGOS\n', '-='*20)
for i in range(rep):
    for c in range(0, 6):
        num.append(random.sample(range(1, 60), 1))
        num.sort()
    print(f'Jogo {i+1}: {num}')
    time.sleep(1)
    num.clear()
print('-='*8, f'BOA SORTE', '-='*8)