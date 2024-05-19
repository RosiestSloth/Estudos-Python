def soma(a, b):

    sm = a + b

    return sm

def subtracao(a, b):

    sb = a - b

    return sb

def multp(a, b):

    mt = a * b

    return mt

def divisao(a, b):

    if b == 0:

        print('Não existe número divisível por zero(0)')

    elif b != 0:

        dv = a / b

    return dv

def menu():

    print('*** Menu de opção ***')

    print(' 1 Soma: ')

    print('2 Subtração: ')

    print('3 Multiplicação: ')

    print('4 Divisão: ')

    print('0 Sair do programa: ')

def main():

    while True:

        menu()

        op = int(input('Digite a opção desejada.\n'))

        ra = int(input('Digite um valor inteiro para o cálculo desejado.\n'))

        rb = int(input('Digite outro valor inteiro para o cálculo desejado.\n'))

        if op == 1:

            print('*** Somar dois valores ***')

            resp = soma(ra, rb)

            print(f'O resultado da soma é {resp}')

        elif op == 2:

            print('*** Subtrair dois valores ***')

            resp = subtracao(ra, rb)

            print(f'O resultado da subtração é {resp}')

        elif op == 3:

            print('*** Multiplicar dois valores ***')

            resp = multp(ra, rb)

            print(f'O resultado a multiplicação é {resp}')

        elif op == 4:

            print('*** Dividir dois valores ***')

            resp = divisao(ra, rb)

            print(f'O resultado da divisão é {resp}') 

        elif op == 0:

            print('saindo do programa...')

            break

 

 

main()