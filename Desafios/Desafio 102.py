def fatorial(num, show=False):
    """
    Uma função que calcula a fatorial de um número
    : param num: O número a ser calculado.
    : param show: (opicional) Mostrar ou não a conta.
    :return: O valor a ser retornado
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} * ', end='')
    return fat

print(fatorial(9))
