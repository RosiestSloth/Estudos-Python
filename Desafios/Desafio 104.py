def leiaInt():
    while True:
        print('-'*30)
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[0;31mDigite um valor válido.\033[m')


n = leiaInt()
print(f'Você digitou o número {n}')