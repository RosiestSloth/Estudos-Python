from time import sleep

def maior(num):
    print('Analisando os valores')
    sleep(1)
    num.sort()
    maior = len(num) - 1
    print('-='*30)
    for c in num:
        print('/', c, end='/')
        sleep(0.5)
    print(f'\nForam digitados {len(num)} valores ao todo')
    print(f'O maior valor digitado foi {num[maior]}\n', '-='*30)


num = []
a = int(input('Digite a quantidade de valores digitados: '))
for i in range(a):
    k = int(input('Digite um valor: '))
    num.append(k)
maior(num)

